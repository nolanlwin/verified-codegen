from __future__ import annotations

import re

from vericode.models import SymbolContext


def validate_spec_semantics(skeleton: str, symbol_context: SymbolContext) -> list[str]:
    """Check that the spec skeleton reflects PR evidence, not just Dafny parse success."""
    issues: list[str] = []
    spec_fn = _extract_primary_spec_function(skeleton)
    if spec_fn is None:
        return issues

    header, body = spec_fn
    params = _param_names(header)

    for param in symbol_context.abstract_parameters:
        if param.dafny_name in params and param.dafny_type == "bool":
            if param.dafny_name not in body and "if " not in body.lower():
                issues.append(
                    f"Spec function should branch on `{param.dafny_name}` ({param.reason})"
                )

    if symbol_context.test_oracles:
        expects_conditional = any(
            "non-empty" in o.expectation.lower()
            or "includes" in o.expectation.lower()
            or "inactive" in o.condition.lower()
            for o in symbol_context.test_oracles
        )
        if expects_conditional and _is_constant_stub_body(body):
            issues.append(
                "Spec function body is a constant stub but PR tests expect conditional behavior"
            )

    markers = [c.marker for c in symbol_context.external_constants]
    if markers and not _is_constant_stub_body(body):
        if not any(marker in body for marker in markers):
            issues.append(
                f"Spec should reference constant marker(s) {markers!r} in the true branch "
                "(opaque sentinels, not full prompt prose)"
            )

    return issues


def format_semantic_issues(issues: list[str]) -> str:
    if not issues:
        return ""
    return "Spec semantic issues:\n" + "\n".join(f"- {issue}" for issue in issues)


def _extract_primary_spec_function(skeleton: str) -> tuple[str, str] | None:
    match = re.search(
        r"(function\s+\w+Spec\s*\([^)]*\)\s*:[^\n]+"
        r"(?:\s*\n\s*(?:requires|decreases)\b[^\n]*)*\s*\{)"
        r"([\s\S]*?^\s*\})",
        skeleton,
        flags=re.MULTILINE,
    )
    if not match:
        return None
    body = match.group(2).strip()
    if body.endswith("}"):
        body = body[:-1].strip()
    return match.group(1), body


def _param_names(header: str) -> list[str]:
    params_match = re.search(r"\(([^)]*)\)", header)
    if not params_match:
        return []
    names: list[str] = []
    for part in params_match.group(1).split(","):
        part = part.strip()
        if not part:
            continue
        names.append(part.split(":")[0].strip())
    return names


def _is_constant_stub_body(body: str) -> bool:
    expr = re.sub(r"//[^\n]*", "", body).strip()
    return expr in {"[]", "0", "false", '""', "''", "0.0"}
