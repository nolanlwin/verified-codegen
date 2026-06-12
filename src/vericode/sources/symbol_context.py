from __future__ import annotations

import ast
import re

from vericode.models import (
    AbstractParameter,
    ExternalConstant,
    ScopedSymbol,
    SymbolContext,
    TaskContext,
    TestOracle,
)

_PYTHON_BUILTINS = {
    "True",
    "False",
    "None",
    "int",
    "str",
    "bool",
    "list",
    "dict",
    "set",
    "tuple",
    "len",
    "range",
    "object",
    "type",
    "isinstance",
    "print",
    "Exception",
}


def analyze_symbol_context(ctx: TaskContext) -> SymbolContext:
    focus = ctx.focus
    if focus is None:
        return SymbolContext()
    if focus.language == "python":
        return _analyze_python(ctx, focus)
    return SymbolContext()


def render_symbol_context_for_prompt(symbol_context: SymbolContext) -> str:
    if not any(
        (
            symbol_context.abstract_parameters,
            symbol_context.external_constants,
            symbol_context.test_oracles,
            symbol_context.unresolved_names,
        )
    ):
        return ""

    parts = ["Derived symbol interface (use for Dafny abstraction, not Python runtime types):"]

    if symbol_context.abstract_parameters:
        parts.append("Abstract parameters:")
        for param in symbol_context.abstract_parameters:
            line = f"- `{param.dafny_name}: {param.dafny_type}`"
            if param.replaces_python_param:
                line += f" replaces Python `{param.replaces_python_param}`"
            if param.reason:
                line += f" — {param.reason}"
            parts.append(line)

    if symbol_context.external_constants:
        parts.append("External constants referenced by the focused symbol:")
        for const in symbol_context.external_constants:
            parts.append(
                f"- `{const.name}` from `{const.defining_path}` "
                f'→ use Dafny seq literal ["{const.marker}"] in spec results (double quotes, not Python single quotes)'
            )
            if const.value_preview:
                parts.append(f"  Preview: {const.value_preview}")

    if symbol_context.test_oracles:
        parts.append("Test oracles from PR tests:")
        for oracle in symbol_context.test_oracles:
            loc = f" ({oracle.source_path})" if oracle.source_path else ""
            parts.append(f"- When {oracle.condition}{loc}: {oracle.expectation}")

    if symbol_context.unresolved_names:
        parts.append(
            "Unresolved identifiers (abstract or note in spec `notes`): "
            + ", ".join(symbol_context.unresolved_names)
        )

    return "\n".join(parts)


def _analyze_python(ctx: TaskContext, focus: ScopedSymbol) -> SymbolContext:
    external_names = _external_names_in_python(focus.source)
    constants: list[ExternalConstant] = []
    unresolved: list[str] = []

    for name in sorted(external_names):
        resolved = _resolve_python_constant(name, ctx)
        if resolved is not None:
            constants.append(resolved)
        else:
            unresolved.append(name)

    abstract_params = _abstract_python_parameters(focus)
    test_oracles = _extract_test_oracles(ctx, focus.name)

    return SymbolContext(
        abstract_parameters=abstract_params,
        external_constants=constants,
        test_oracles=test_oracles,
        unresolved_names=unresolved,
    )


def _external_names_in_python(source: str) -> set[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()

    assigned: set[str] = set()
    loaded: set[str] = set()
    param_names: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            for arg in node.args.args + node.args.kwonlyargs:
                param_names.add(arg.arg)
            if node.args.vararg:
                param_names.add(node.args.vararg.arg)
            if node.args.kwarg:
                param_names.add(node.args.kwarg.arg)

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):
                assigned.add(node.id)
            elif isinstance(node.ctx, ast.Load):
                loaded.add(node.id)

    return loaded - assigned - param_names - _PYTHON_BUILTINS


def _resolve_python_constant(name: str, ctx: TaskContext) -> ExternalConstant | None:
    for fc in ctx.files:
        text = fc.after or fc.before
        if not text or name not in text:
            continue

        marker = _marker_from_constant_text(text, name)
        if marker is None:
            continue

        preview = _preview_constant(text, name)
        return ExternalConstant(
            name=name,
            defining_path=fc.path,
            marker=marker,
            value_preview=preview,
        )

    return None


def _marker_from_constant_text(text: str, name: str) -> str | None:
    triple = re.search(
        rf'^{re.escape(name)}\s*=\s*"""(.*?)"""',
        text,
        re.MULTILINE | re.DOTALL,
    )
    if triple:
        body = triple.group(1)
        tag = re.search(r"<(\w+)>", body)
        if tag:
            return tag.group(1)
        first_line = next((ln.strip() for ln in body.splitlines() if ln.strip()), "")
        if first_line:
            return _slugify(first_line[:48])
        return name.lower()

    single = re.search(
        rf"^{re.escape(name)}\s*=\s*'''(.*?)'''",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if single:
        body = single.group(1)
        tag = re.search(r"<(\w+)>", body)
        if tag:
            return tag.group(1)
        return name.lower()

    one_line = re.search(rf'^{re.escape(name)}\s*=\s*["\']([^"\']+)["\']', text, re.MULTILINE)
    if one_line:
        return _slugify(one_line.group(1))

    return None


def _preview_constant(text: str, name: str) -> str:
    triple = re.search(
        rf'^{re.escape(name)}\s*=\s*"""(.*?)"""',
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not triple:
        return ""
    body = triple.group(1).strip().replace("\n", " ")
    return body[:120] + ("…" if len(body) > 120 else "")


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.lower()).strip("_")
    return slug[:48] or "value"


def _abstract_python_parameters(focus: ScopedSymbol) -> list[AbstractParameter]:
    params: list[AbstractParameter] = []
    source = focus.source

    python_params = _python_param_names(source)
    config_params = [p for p in python_params if "config" in p.lower()]
    if not config_params:
        return params

    gates = _config_presence_gates(source)
    if not gates:
        return params

    for gate_key, reason in gates:
        params.append(
            AbstractParameter(
                dafny_name=f"has_{gate_key}",
                dafny_type="bool",
                replaces_python_param=config_params[0],
                reason=reason,
            )
        )
    return params


def _python_param_names(source: str) -> list[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            return [arg.arg for arg in node.args.args]
    return []


def _config_presence_gates(source: str) -> list[tuple[str, str]]:
    gates: list[tuple[str, str]] = []
    seen: set[str] = set()

    patterns = [
        (
            r'\.get\(\s*["\'](\w+)["\']\s*\)\s+is\s+not\s+None',
            "configurable[{key}] is present",
        ),
        (
            r'\.get\(\s*["\'](\w+)["\']\s*\)\s+is\s+None',
            "configurable[{key}] is absent",
        ),
        (
            r'if\s+\(?.*\.get\(\s*["\'](\w+)["\']\s*\).*\):',
            "truthiness of configurable[{key}]",
        ),
    ]
    for pattern, template in patterns:
        for match in re.finditer(pattern, source):
            key = match.group(1)
            if key in seen:
                continue
            seen.add(key)
            gates.append((key, template.format(key=key)))

    return gates


def _extract_test_oracles(ctx: TaskContext, symbol_name: str) -> list[TestOracle]:
    oracles: list[TestOracle] = []
    keywords = _test_keywords_for_symbol(symbol_name)

    for fc in ctx.files:
        if "test" not in fc.path.lower():
            continue
        if fc.patch and (
            symbol_name in fc.patch or any(keyword in fc.patch for keyword in keywords)
        ):
            combined = _patch_added_lines(fc.patch)
        else:
            combined = f"{fc.patch}\n{fc.after}"
        blocks = _relevant_test_blocks(combined, symbol_name, keywords)
        if not blocks:
            continue

        for block in blocks:
            for match in re.finditer(r'assertIn\(\s*["\']([^"\']+)["\']', block):
                oracles.append(
                    TestOracle(
                        condition="context is active (per focused PR test)",
                        expectation=f"combined output includes {match.group(1)!r}",
                        source_path=fc.path,
                    )
                )
            for match in re.finditer(r'assertNotIn\(\s*["\']([^"\']+)["\']', block):
                oracles.append(
                    TestOracle(
                        condition="context is inactive (per focused PR test)",
                        expectation=f"combined output must not include {match.group(1)!r}",
                        source_path=fc.path,
                    )
                )

            if re.search(r"from_slack|should_contain", block):
                oracles.append(
                    TestOracle(
                        condition="parameterized cases distinguish active vs inactive context",
                        expectation="return value is non-empty iff context is active",
                        source_path=fc.path,
                    )
                )

    deduped: list[TestOracle] = []
    seen: set[tuple[str, str]] = set()
    for oracle in oracles:
        key = (oracle.condition, oracle.expectation)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(oracle)
    return deduped[:8]


def _patch_added_lines(patch: str) -> str:
    return "\n".join(
        line[1:]
        for line in patch.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    )


def _test_keywords_for_symbol(symbol_name: str) -> list[str]:
    stem = symbol_name.lstrip("_")
    parts = [p for p in re.split(r"_+", stem) if len(p) > 3]
    return [stem, *parts]


def _relevant_test_blocks(combined: str, symbol_name: str, keywords: list[str]) -> list[str]:
    blocks: list[str] = []
    pattern = re.compile(
        r"(?:async\s+)?def\s+(test_\w+)\s*\([^)]*\):[\s\S]*?(?=\n(?:async\s+)?def\s+test_|\Z)",
        re.MULTILINE,
    )
    for match in pattern.finditer(combined):
        block = match.group(0)
        test_name = match.group(1)
        if symbol_name in block or any(keyword in test_name or keyword in block for keyword in keywords):
            blocks.append(block)
    if not blocks and symbol_name in combined:
        blocks.append(combined)
    return blocks
