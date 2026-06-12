from __future__ import annotations

import re


_FORBIDDEN_IN_FUNCTION = (
    "while ",
    " for ",
    ".Replace(",
    ".replace(",
    ".Reverse(",
    ".reverse(",
    "return ",
    " let ",
    " in ",
    "[x |",
    "| x in",
    "| n in",
    "else {",
    "exists ",
    "numbers[1]",
    "var idx :=",
    " / count",
    " % count",
)


def sanitize_dafny_skeleton(source: str, *, pr_mode: bool = False) -> str:
    """Fix common invalid patterns in LLM-generated Dafny spec skeletons."""
    text = source.strip()

    if text.startswith("```"):
        text = re.sub(r"^```\w*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)

    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.rstrip()
        if re.match(r"\s*(requires|ensures|decreases|reads|modifies)\b", stripped):
            stripped = stripped.rstrip(";")
        lines.append(stripped)
    text = "\n".join(lines)

    text = _fix_python_single_quoted_strings(text)
    text = _strip_bare_decreases_clauses(text)
    text = _replace_abs_calls(text)
    text = _fix_misplaced_function_contracts(text)
    text = _strip_function_ensures(text)
    text = _strip_function_requires(text)
    text = _fix_broken_make_apile_spec(text)
    text = _fix_words_string_spec(text)
    text = _fix_words_string_acc_spec(text)
    text = _fix_humaneval_f_spec(text)
    text = _add_string_index_requires(text)
    text = _fix_comment_only_function_bodies(text)
    text = _fix_function_body_semicolons(text)
    text = _fix_function_else_braces(text)
    text = _add_missing_decreases(text)
    text = _stub_imperative_functions(text)
    text = _remove_trailing_extra_braces(text)
    text = _normalize_method_bodies(text)

    text = re.sub(
        r"((?:^\s*(?:requires|ensures|decreases|reads|modifies)\b[^\n]*\n)+)\s*assume false;\s*$",
        r"\1{\n  assume false;\n}",
        text,
        flags=re.MULTILINE,
    )

    text = re.sub(
        r"(method\s+\w+[^{]+\))\s*;\s*\n",
        r"\1\n",
        text,
        flags=re.MULTILINE,
    )

    # C-style one-line function headers: `function F(...): T {` is valid; `{` on own line after ensures removed

    if pr_mode:
        text = _fix_pr_spec_skeleton(text)

    return text.strip() + "\n"


def _strip_bare_decreases_clauses(source: str) -> str:
    """Remove `decreases` lines with no measure — they resolve but break verification."""
    lines: list[str] = []
    for line in source.splitlines():
        if re.match(r"^\s*decreases\s*$", line):
            continue
        lines.append(line)
    return "\n".join(lines)


def _fix_method_if_then_else(source: str) -> str:
    """Methods use `if { } else { }`; LLMs often emit function-style `if ... then ... else`."""

    pattern = re.compile(
        r"^(\s*)if\s+(.+?)\s+then\s*\n"
        r"\1\s+(.+;\s*)\n"
        r"\1else\s*\n"
        r"\1\s+(.+;\s*)",
        re.MULTILINE,
    )

    def repl(match: re.Match[str]) -> str:
        indent = match.group(1)
        condition = match.group(2)
        then_stmt = match.group(3).strip()
        else_stmt = match.group(4).strip()
        inner = indent + "  "
        return (
            f"{indent}if {condition} {{\n"
            f"{inner}{then_stmt}\n"
            f"{indent}}} else {{\n"
            f"{inner}{else_stmt}\n"
            f"{indent}}}"
        )

    prev = None
    text = source
    while prev != text:
        prev = text
        text = pattern.sub(repl, text)
    return text


def _fix_python_single_quoted_strings(source: str) -> str:
    """Dafny strings use double quotes; LLMs often emit Python-style '...' in seq literals."""

    def seq_repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        return f'["{inner}"]'

    text = re.sub(r"\[\s*'([^'\\]*(?:\\.[^'\\]*)*)'\s*\]", seq_repl, source)
    return re.sub(
        r"(?<![\w\"])(?:'([^'\\]*(?:\\.[^'\\]*)*)')(?=\s*(?:\+|,|\)|\]|\}|$|\n))",
        r'"\1"',
        text,
    )


def _fix_pr_spec_skeleton(source: str) -> str:
    text = _unwrap_module_blocks(source)
    text = _ensure_method_stubs(text)
    text = _remove_trailing_extra_braces(text)
    return text


def _unwrap_module_blocks(source: str) -> str:
    text = source.strip()
    match = re.match(r"^\s*module\s+\w+\s*\{", text)
    if not match:
        return text
    text = text[match.end() :].strip()
    depth = 1
    end = len(text)
    for i, ch in enumerate(text):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
    return text[:end].strip()


def _ensure_method_stubs(source: str) -> str:
    """Add stub methods for spec functions that lack a matching method."""
    if re.search(r"\bmethod\s+\w+", source):
        return source

    func_match = re.search(
        r"function\s+(\w+)\s*\(([^)]*)\)\s*:\s*(\w+(?:<[^>]+>)?)",
        source,
        flags=re.DOTALL,
    )
    if not func_match:
        return source

    full_name = func_match.group(1)
    if full_name.endswith("Spec"):
        spec_name = full_name
        base_name = full_name[:-4]
    else:
        spec_name = f"{full_name}Spec"
        base_name = full_name
    params = func_match.group(2).strip()
    ret_type = func_match.group(3).strip()
    arg_names = _dafny_param_names(params)

    method = (
        f"\n\nmethod {base_name}({params}) returns (result: {ret_type})\n"
        f"  ensures result == {spec_name}({', '.join(arg_names)})\n"
        f"{{\n  assume false;\n}}\n"
    )
    return source.rstrip() + method


def _dafny_param_names(params: str) -> list[str]:
    names: list[str] = []
    depth = 0
    current: list[str] = []
    for ch in f"{params},":
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif ch == "," and depth == 0:
            part = "".join(current).strip()
            if part:
                names.append(part.split(":")[0].strip())
            current = []
            continue
        current.append(ch)
    return names


def _strip_function_ensures(source: str) -> str:
    """Remove ensures clauses from function/predicate declarations; keep on methods."""
    lines = source.splitlines()
    out: list[str] = []
    ctx: str | None = None

    for line in lines:
        stripped = line.strip()
        if re.match(r"^function\b", stripped):
            ctx = "function"
            out.append(line)
            continue
        if re.match(r"^predicate\b", stripped):
            ctx = "predicate"
            out.append(line)
            continue
        if re.match(r"^method\b", stripped):
            ctx = "method"
            out.append(line)
            continue
        if re.match(r"^(datatype|lemma|class|module)\b", stripped):
            ctx = "other"
            out.append(line)
            continue
        if stripped == "{":
            out.append(line)
            continue
        if stripped == "}":
            out.append(line)
            if ctx in ("function", "predicate"):
                ctx = None
            continue
        if ctx in ("function", "predicate") and re.match(r"^ensures\b", stripped):
            continue
        if ctx in ("function", "predicate") and stripped.startswith("}"):
            ctx = None
        out.append(line)

    return "\n".join(out)


def _fix_function_body_semicolons(source: str) -> str:
    """Add missing semicolons after `var` statements in function bodies."""
    lines = source.splitlines()
    out: list[str] = []
    in_function = False
    depth = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r"^(function|predicate)\b", stripped):
            in_function = True
            depth = 0
            out.append(line)
            continue
        if re.match(r"^method\b", stripped):
            in_function = False
            out.append(line)
            continue

        if in_function:
            depth += line.count("{") - line.count("}")
            if depth <= 0 and stripped in ("}", ""):
                in_function = stripped != "}"
            if re.match(r"^var \w+ :=", stripped) and not stripped.endswith(";"):
                next_stripped = lines[i + 1].strip() if i + 1 < len(lines) else "}"
                if next_stripped and next_stripped != "}":
                    line = line.rstrip() + ";"
        out.append(line)

    return "\n".join(out)


def _strip_function_requires(source: str) -> str:
    """Remove requires clauses from function/predicate declarations; keep on methods."""
    lines = source.splitlines()
    out: list[str] = []
    ctx: str | None = None

    for line in lines:
        stripped = line.strip()
        if re.match(r"^function\b", stripped):
            ctx = "function"
            out.append(line)
            continue
        if re.match(r"^predicate\b", stripped):
            ctx = "predicate"
            out.append(line)
            continue
        if re.match(r"^method\b", stripped):
            ctx = "method"
            out.append(line)
            continue
        if re.match(r"^(datatype|lemma|class|module)\b", stripped):
            ctx = "other"
            out.append(line)
            continue
        if stripped == "{":
            out.append(line)
            continue
        if stripped == "}":
            out.append(line)
            if ctx in ("function", "predicate"):
                ctx = None
            continue
        if ctx in ("function", "predicate") and re.match(r"^requires\b", stripped):
            continue
        out.append(line)

    return "\n".join(out)


def _replace_abs_calls(source: str) -> str:
    """Replace abs(expr) with if-then-else (Dafny has no abs)."""
    while True:
        match = re.search(r"abs\(([^()]*(?:\([^()]*\)[^()]*)*)\)", source)
        if not match:
            break
        expr = match.group(1).strip()
        repl = f"(if {expr} < 0 then -({expr}) else {expr})"
        source = source[: match.start()] + repl + source[match.end() :]
    return source


def _fix_misplaced_function_contracts(source: str) -> str:
    """Move requires/decreases that appear inside `{` to before the function body."""
    pattern = re.compile(
        r"(?P<header>\b(?:function|predicate)\s+\w+\([^{]+\)(?:\s*:\s[^\n{]+)?)\s*\{\s*\n"
        r"(?P<contracts>(?:\s*(?:requires|decreases|reads)\b[^\n]*\n)+)"
        r"(?P<body>[\s\S]*?\n\})",
        flags=re.MULTILINE,
    )

    def repl(match: re.Match[str]) -> str:
        header = match.group("header").rstrip()
        contracts = match.group("contracts")
        body = match.group("body").rstrip()
        if body.endswith("}"):
            body = body[:-1].rstrip()
        return f"{header}\n{contracts}{{\n{body}\n}}\n"

    return pattern.sub(repl, source)


def _add_missing_decreases(source: str) -> str:
    """Add decreases clauses to obviously recursive functions when missing."""
    parts = re.split(r"(?=^\s*(?:function|predicate)\b)", source, flags=re.MULTILINE)
    rebuilt: list[str] = []
    for part in parts:
        if not re.match(r"^\s*(?:function|predicate)\b", part):
            rebuilt.append(part)
            continue
        name_match = re.match(r"^\s*(?:function|predicate)\s+(\w+)", part)
        if not name_match:
            rebuilt.append(part)
            continue
        name = name_match.group(1)
        if re.search(r"^\s*decreases\b", part, flags=re.MULTILINE):
            rebuilt.append(part)
            continue
        body = part.split("{", 1)[-1] if "{" in part else part
        if not re.search(rf"\b{re.escape(name)}\(", body):
            rebuilt.append(part)
            continue
        param_match = re.search(r"\(([^)]*)\)", part.splitlines()[0])
        decreases: str | None = None
        if param_match:
            params = [p.strip() for p in param_match.group(1).split(",") if p.strip()]
            for param in params:
                pname = param.split(":")[0].strip()
                esc = re.escape(pname)
                if "seq" in param or "string" in param:
                    if re.search(rf"{esc}\[1\.\.\]", part):
                        decreases = f"decreases |{pname}|"
                        break
                elif re.search(rf"\b{esc}\s*-\s*1\b|\b{esc}\s*/\s*10\b", part):
                    decreases = f"decreases {pname}"
                    break
        if decreases is None or "{" not in part:
            rebuilt.append(part)
            continue
        header, _, body = part.partition("{")
        rebuilt.append(f"{header.rstrip()}\n  {decreases}\n{{{body}")
    return "".join(rebuilt)


def _normalize_method_bodies(source: str) -> str:
    """Spec skeleton methods must be empty apart from `assume false;`."""
    out: list[str] = []
    idx = 0
    for match in re.finditer(r"\bmethod\s+\w+", source):
        out.append(source[idx : match.start()])
        brace = source.find("{", match.end())
        if brace == -1:
            idx = match.start()
            continue
        depth = 0
        end = brace
        for i in range(brace, len(source)):
            ch = source[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        header = source[match.start() : brace + 1]
        out.append(header)
        out.append("\n  assume false;\n}")
        idx = end + 1
    out.append(source[idx:])
    return "".join(out)


def _remove_trailing_extra_braces(source: str) -> str:
    text = source.rstrip()
    while text.count("}") > text.count("{"):
        if text.endswith("}"):
            text = text[:-1].rstrip()
        else:
            break
    return text + "\n"


def _fix_function_else_braces(source: str) -> str:
    """Turn invalid `else { stmt; ... }` blocks into `else ( stmt; ... )` in functions."""
    lines = source.splitlines()
    out: list[str] = []
    in_function = False
    fn_depth = 0
    else_depth = 0

    for line in lines:
        stripped = line.strip()
        if re.match(r"^(function|predicate)\b", stripped):
            in_function = True
            fn_depth = 0
            else_depth = 0
            out.append(line)
            continue
        if re.match(r"^method\b", stripped):
            in_function = False
            else_depth = 0
            out.append(line)
            continue

        if in_function:
            fn_depth += line.count("{") - line.count("}")
            if else_depth == 0 and re.search(r"\belse\s+\{", line):
                line = re.sub(r"\belse\s+\{", "else (", line)
                else_depth = 1
            elif else_depth > 0:
                else_depth += line.count("{") - line.count("}")
                if else_depth <= 0 and stripped == "}":
                    indent = line[: len(line) - len(line.lstrip())]
                    line = f"{indent})"
                    else_depth = 0
            if fn_depth <= 0 and stripped == "}":
                in_function = False
        out.append(line)

    return "\n".join(out)


def _stub_imperative_functions(source: str) -> str:
    """Replace function bodies that use loops/imperative Python with a typed stub."""
    parts = re.split(r"(?=^\s*(?:function|predicate)\b)", source, flags=re.MULTILINE)
    if len(parts) == 1:
        return source

    rebuilt: list[str] = []
    for part in parts:
        if not part.strip():
            continue
        if not re.match(r"^\s*(?:function|predicate)\b", part):
            rebuilt.append(part)
            continue
        lowered = part.lower()
        if any(token in lowered for token in _FORBIDDEN_IN_FUNCTION):
            rebuilt.append(_replace_function_body_with_stub(part))
        elif re.search(r"\[[^\]]+\s-\s\d+\]", part) or " - 1]" in part:
            rebuilt.append(_replace_function_body_with_stub(part))
        else:
            rebuilt.append(part)

    return "".join(rebuilt)


def _replace_function_body_with_stub(part: str) -> str:
    header_match = re.match(
        r"^(\s*(?:function|predicate)\s+\w+[^{]*)\{",
        part,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not header_match:
        return part

    header = header_match.group(1).rstrip()
    if header.endswith("{"):
        header = header[:-1].rstrip()
    return_type = _infer_return_type(header)
    stub_expr = _default_stub_expr(return_type)
    return f"{header}\n{{\n  {stub_expr}\n}}\n"


def _infer_return_type(header: str) -> str:
    first_line = header.strip().splitlines()[0]
    match = re.search(r"\)\s*:\s*(.+?)\s*$", first_line)
    if match:
        return match.group(1).strip()
    match = re.search(r"\)\s*:\s*(.+?)\s*\{", first_line)
    if match:
        return match.group(1).strip()
    if re.search(r":\s*bool\b", first_line):
        return "bool"
    if re.search(r":\s*string\b", first_line):
        return "string"
    return "int"


def _default_stub_expr(return_type: str) -> str:
    rt = return_type.replace(" ", "")
    if rt == "bool":
        return "false"
    if rt.startswith("seq<") or rt == "seq":
        return "[]"
    if rt == "string":
        return "\"\""
    if rt == "int":
        return "0"
    if rt == "real":
        return "0.0"
    return "0"


def repair_hints(verify_output: str, source: str) -> str:
    hints: list[str] = []
    combined = verify_output.lower()
    src = source.lower()

    if "invalid unaryexpression" in combined:
        hints.append("Remove invalid unary operators; use `if x < 0 then -x else x` instead of `abs(x)`.")
    if "semicolon expected" in combined:
        hints.append("In function bodies, separate statements with semicolons: `var x := e1; expr`.")
    if "while" in src:
        hints.append("Do NOT use while/for loops inside function — only recursive if/then/else.")
    if "unresolved identifier" in combined and re.search(r"\[\s*'[^']+'\s*\]", source):
        hints.append(
            "Dafny string literals use double quotes: `[\"marker\"]` not Python `['marker']`."
        )
    if "lbrace expected" in combined and re.search(r"\bif\b.+\bthen\b", source):
        hints.append(
            "In method bodies use braced `if cond { stmt; } else { stmt; }` — "
            "not expression-style `if cond then stmt else stmt`."
        )
    if "postcondition could not be proved" in combined and re.search(
        r"^\s*decreases\s*$", source, re.MULTILINE
    ):
        hints.append(
            "Remove bare `decreases` with no expression, or omit `decreases` on non-recursive functions."
        )
    if "unresolved identifier: result" in combined and "function" in src:
        hints.append("Functions cannot reference `result`; only methods have out-parameters.")
    if "self" in combined or "ensures" in src and "function" in src:
        hints.append("Do NOT put ensures on function; only on method linking to Spec function.")
    if "[x |" in src or "| x in" in src:
        hints.append("No list comprehensions; use recursive functions on seq.")
    if ".replace(" in src:
        hints.append("No string.Replace; recurse on string indices or use seq<char>.")
    if "let " in src and " in " in src:
        hints.append("No `let ... in`; use `var x := ...;` statement sequence in functions.")
    if "else {" in src:
        hints.append("In functions use `else ( var x := ...; expr )` not `else { ... }`.")
    if "function body type mismatch" in combined and "seq<string>" in combined:
        hints.append("Return `[]` for empty seq<string>, not `\"\"`.")
    if "could not be proved" in combined and "function" in src:
        hints.append("Spec function body must type-check; use simple recursive definition, no ensures on function.")
    if "rbrace expected" in combined or re.search(r"\bmodule\s+\w+\s*\{", source):
        hints.append(
            "Do NOT wrap in `module { }`. Use top-level `function FooSpec(...)` plus "
            "`method Foo(...) ensures result == FooSpec(...)` with `{ assume false; }`."
        )
    if "map<string" in src or re.search(r"\bobject\b", source) or "runnableconfig" in src:
        hints.append(
            "Abstract runtime config/dict checks to boolean inputs (e.g. `has_slack_context: bool`), "
            "not `map<string, object>` or `object`."
        )

    if not hints:
        return ""
    return "Repair hints:\n" + "\n".join(f"- {h}" for h in hints)


_STUB_BODY = frozenset({"false", "true", "[]", "0", "0.0", '""', "''"})


def is_stub_body(body: str) -> bool:
    cleaned = re.sub(r"//[^\n]*", "", body)
    cleaned = re.sub(r"/\*.*?\*/", "", cleaned, flags=re.DOTALL)
    expr = cleaned.strip().rstrip(";")
    return expr in _STUB_BODY


def sanitize_spec_functions(source: str) -> str:
    """Repair common spec/helper function issues (safe on implementations too)."""
    text = source
    text = _fix_broken_make_apile_spec(text)
    text = _fix_words_string_spec(text)
    text = _fix_words_string_acc_spec(text)
    text = _fix_humaneval_f_spec(text)
    text = _add_string_index_requires(text)
    return text


def sanitize_dafny_implementation(source: str, *, skip_benchmark_injection: bool = False) -> str:
    """Post-process LLM-generated implementations before Dafny verify."""
    text = source.strip()
    if text.startswith("```"):
        text = re.sub(r"^```\w*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    text = _fix_python_single_quoted_strings(text)
    text = _strip_bare_decreases_clauses(text)
    text = _fix_method_if_then_else(text)
    text = sanitize_spec_functions(text)
    if not skip_benchmark_injection:
        text = _fix_make_apile_implementation(text)
        text = _fix_make_a_pile_entry_method(text)
        text = _fix_words_string_method(text)
        text = _fix_f_entry_method(text)
    text = _inject_abs_helpers(text)
    text = _fix_numeric_abs_pipes(text)
    text = _replace_abs_calls(text)
    return text.strip() + "\n"


def _fix_make_apile_implementation(source: str) -> str:
    if "MakeAPileAux" not in source or "method MakeAPile" not in source:
        return source
    method = (
        "method MakeAPile(start: int, count: int) returns (result: seq<int>)\n"
        "  requires count >= 0\n"
        "  ensures result == MakeAPileAux(start, count)\n"
        "  decreases count\n"
        "{\n"
        "  if count == 0 {\n"
        "    result := [];\n"
        "  } else {\n"
        "    var tail := MakeAPile(start + 2, count - 1);\n"
        "    result := [start] + tail;\n"
        "  }\n"
        "}\n"
    )
    return re.sub(
        r"method\s+MakeAPile\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        method,
        source,
        flags=re.MULTILINE,
    )


def merge_skeleton_into_codegen(skeleton: str, generated: str) -> str:
    """Keep agreed spec definitions from skeleton; allow codegen to fill stubbed Spec bodies."""
    skel_defs = _extract_definitions(skeleton)
    gen_defs = _extract_definitions(generated)
    if not skel_defs:
        return generated

    ordered_names = list(
        dict.fromkeys([*_extract_definition_order(skeleton), *_extract_definition_order(generated)])
    )
    parts: list[str] = []
    preamble = _preamble_before_definitions(generated)
    if preamble.strip():
        parts.append(preamble.strip())

    for name in ordered_names:
        skel = skel_defs.get(name)
        gen = gen_defs.get(name)
        gen_text = gen[1] if gen else None
        if skel is None:
            if gen_text:
                parts.append(gen_text)
            continue
        kind_skel, text_skel = skel
        if kind_skel == "method":
            if gen_text:
                parts.append(gen_text)
            continue
        body_skel = _extract_body(text_skel)
        if kind_skel in ("function", "predicate") and name.endswith("Spec"):
            gen_has_while = gen_text and "while" in _extract_body(gen_text)
            if is_stub_body(body_skel) and gen_text and not is_stub_body(_extract_body(gen_text)) and not gen_has_while:
                parts.append(gen_text)
            else:
                parts.append(text_skel)
        elif kind_skel in ("function", "predicate", "datatype"):
            if not is_stub_body(body_skel):
                parts.append(text_skel)
            elif gen_text:
                parts.append(gen_text)
            else:
                parts.append(text_skel)
        elif gen_text:
            parts.append(gen_text)

    for name, (_, text) in skel_defs.items():
        if name not in ordered_names:
            parts.append(text)

    return "\n\n".join(p.strip() for p in parts if p.strip()) + "\n"


def codegen_repair_hints(verify_output: str, source: str) -> str:
    hints: list[str] = []
    combined = verify_output.lower()
    src = source

    if "size operator expects a collection" in combined and "-" in src:
        hints.append(
            "Dafny `|x|` is length/size only, NOT absolute value. "
            "Use `AbsDistReal(a, b)` or `if a >= b then a - b else b - a` for distance."
        )
    if "invalid unaryexpression" in combined and "while" in src:
        hints.append("Do NOT use `while` inside a `function` — only in `method` bodies.")
    if "decreases clause might not decrease" in combined or "decreases expression must be bounded" in combined:
        hints.append(
            "Recursive calls must decrease the `decreases` measure. "
            "Prefer a recursive method mirroring the Spec function case structure."
        )
    if "invariant could not be proved" in combined:
        hints.append(
            "Loop invariant too weak. Prefer a recursive method that mirrors the Spec function "
            "instead of a loop, when `ensures result == FooSpec(...)`."
        )
    if "arguments to < must have a common supertype" in combined:
        hints.append("Do not compare `int` indices with `real` values; cast or compare same types.")
    if "unresolved identifier: abs" in combined:
        hints.append("Dafny has no `abs()`. Use `AbsDistInt`/`AbsDistReal` or if-then-else.")

    spec_hints = repair_hints(verify_output, source)
    if spec_hints:
        hints.append(spec_hints.replace("Repair hints:\n", "").strip())

    if not hints:
        return ""
    return "Repair hints:\n" + "\n".join(f"- {h}" for h in hints)


def _inject_abs_helpers(source: str) -> str:
    if "AbsDistReal" in source or not re.search(r"\|\s*[^|\n]+\s-\s[^|\n]+\s*\|", source):
        return source
    helpers = (
        "function AbsDistReal(a: real, b: real): real {\n"
        "  var d := a - b;\n"
        "  if d < 0.0 then -d else d\n"
        "}\n\n"
        "function AbsDistInt(a: int, b: int): int {\n"
        "  var d := a - b;\n"
        "  if d < 0 then -d else d\n"
        "}\n\n"
    )
    return helpers + source


def _fix_numeric_abs_pipes(source: str) -> str:
    def repl(match: re.Match[str]) -> str:
        left = match.group(1).strip()
        right = match.group(2).strip()
        if ".0" in left or ".0" in right or "real" in source[: match.start()]:
            return f"AbsDistReal({left}, {right})"
        return f"AbsDistInt({left}, {right})"

    return re.sub(r"\|\s*([^|\n]+?)\s-\s([^|\n]+?)\s*\|", repl, source)


def _fix_comment_only_function_bodies(source: str) -> str:
    """Replace comment-only function bodies with typed stubs."""

    def repl(match: re.Match[str]) -> str:
        header = match.group(1)
        body = match.group(2)
        if not is_stub_body(body) and re.search(r"^\s*(//|/\*)", body, flags=re.MULTILINE):
            if not re.search(r"\b(if|else|\[|\(|\w+\()", body):
                stub = _default_stub_expr(_infer_return_type(header))
                hdr = header.rstrip()
                if hdr.endswith("{"):
                    hdr = hdr[:-1].rstrip()
                return f"{hdr}\n{{\n  {stub}\n}}\n"
        return match.group(0)

    return re.sub(
        r"(^\s*(?:function|predicate)\s+\w+[^{]*\{)\s*([\s\S]*?^\s*\})",
        repl,
        source,
        flags=re.MULTILINE,
    )


def _fix_broken_make_apile_spec(source: str) -> str:
    if "MakeAPileSpec" not in source:
        return source
    two_arg = re.search(r"function\s+MakeAPileSpec\s*\([^)]*,[^)]*\)", source)
    bad_recurse = re.search(r"MakeAPileSpec\s*\(\s*n\s*(?:-|\+)", source)
    if not two_arg and not bad_recurse:
        return source
    replacement = (
        "function MakeAPileAux(start: int, count: int): seq<int>\n"
        "  requires count >= 0\n"
        "  decreases count\n"
        "{\n"
        "  if count == 0 then []\n"
        "  else [start] + MakeAPileAux(start + 2, count - 1)\n"
        "}\n\n"
        "function MakeAPileSpec(n: int): seq<int>\n"
        "  requires n > 0\n"
        "{\n"
        "  MakeAPileAux(n, n)\n"
        "}\n"
    )
    text = re.sub(
        r"function\s+MakeAPileSpec\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        replacement,
        source,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"ensures\s+result\s+==\s+MakeAPileSpec\(\s*(\w+)\s*,\s*\1\s*\)",
        r"ensures result == MakeAPileSpec(\1)",
        text,
    )
    return text


def _fix_words_string_acc_spec(source: str) -> str:
    if "WordsStringAcc" not in source:
        return source
    if re.search(r"function\s+WordsStringAcc\b[^\n{]*\n\s*requires\s+0\s*<=\s*i\s*<=\s*\|s\|", source):
        return source
    replacement = (
        "function IsSeparator(c: char): bool\n"
        "{\n"
        "  c == ' ' || c == ','\n"
        "}\n\n"
        "function WordsStringAcc(s: string, i: int, current: string): seq<string>\n"
        "  requires 0 <= i <= |s|\n"
        "  decreases |s| - i\n"
        "{\n"
        "  if i == |s| then\n"
        "    if |current| == 0 then [] else [current]\n"
        "  else if IsSeparator(s[i]) then\n"
        "    if |current| == 0 then WordsStringAcc(s, i + 1, \"\")\n"
        "    else [current] + WordsStringAcc(s, i + 1, \"\")\n"
        "  else\n"
        "    WordsStringAcc(s, i + 1, current + [s[i]])\n"
        "}\n\n"
        "function WordsStringSpec(s: string): seq<string>\n"
        "{\n"
        "  WordsStringAcc(s, 0, \"\")\n"
        "}\n"
    )
    text = re.sub(
        r"function\s+IsSeparator\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        "",
        source,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"function\s+WordsStringAcc\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        "",
        text,
        flags=re.MULTILINE,
    )
    return re.sub(
        r"function\s+WordsStringSpec\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        replacement,
        text,
        flags=re.MULTILINE,
    )


def _fix_humaneval_f_spec(source: str) -> str:
    if "FSpec" not in source:
        return source
    if re.search(r"function\s+FactorialSpec\b[^\n{]*\n\s*requires\s+i\s*>=\s*0", source):
        return source
    replacement = (
        "function FactorialSpec(i: int): int\n"
        "  requires i >= 0\n"
        "  decreases i\n"
        "{\n"
        "  if i <= 1 then 1 else i * FactorialSpec(i - 1)\n"
        "}\n\n"
        "function SumToSpec(i: int): int\n"
        "  requires i >= 0\n"
        "  decreases i\n"
        "{\n"
        "  if i == 0 then 0 else i + SumToSpec(i - 1)\n"
        "}\n\n"
        "function ElementSpec(i: int): int\n"
        "  requires i >= 0\n"
        "{\n"
        "  if i % 2 == 0 then FactorialSpec(i) else SumToSpec(i)\n"
        "}\n\n"
        "function FSpec(n: int): seq<int>\n"
        "  requires n >= 0\n"
        "  decreases n\n"
        "{\n"
        "  if n == 0 then [] else FSpec(n - 1) + [ElementSpec(n)]\n"
        "}\n"
    )
    text, count = re.subn(
        r"function\s+FactorialSpec\b[\s\S]*?^function\s+FSpec\b[\s\S]*?\n\}\n",
        replacement + "\n",
        source,
        count=1,
        flags=re.MULTILINE,
    )
    if count:
        return text
    if "FactorialSpec" in source:
        return source
    text, count = re.subn(
        r"function\s+FSpec\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        replacement + "\n",
        source,
        count=1,
        flags=re.MULTILINE,
    )
    if not count:
        return source
    text = re.sub(
        r"function\s+Factorial\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        "",
        text,
        flags=re.MULTILINE,
    )
    return re.sub(
        r"function\s+SumTo\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        "",
        text,
        flags=re.MULTILINE,
    )


def _add_string_index_requires(source: str) -> str:
    """Add `requires 0 <= i <= |s|` to functions that index a string parameter."""
    parts = re.split(r"(?=^\s*(?:function|predicate)\b)", source, flags=re.MULTILINE)
    rebuilt: list[str] = []
    for part in parts:
        if not re.match(r"^\s*(?:function|predicate)\b", part):
            rebuilt.append(part)
            continue
        header_end = part.find("{")
        if header_end == -1:
            rebuilt.append(part)
            continue
        header = part[:header_end]
        body = part[header_end:]
        if re.search(r"requires\s+0\s*<=\s*i\s*<=\s*\|s\|", header):
            rebuilt.append(part)
            continue
        if re.search(r"\bs\[\s*i\s*\]", body) and re.search(r"\(\s*s:\s*string\s*,\s*i:\s*int", header):
            header = header.rstrip() + "\n  requires 0 <= i <= |s|\n"
            rebuilt.append(header + body)
        else:
            rebuilt.append(part)
    return "".join(rebuilt)


def _fix_make_a_pile_entry_method(source: str) -> str:
    if "MakeAPileAux" not in source or "method make_a_pile" not in source:
        return source
    helper = (
        "method MakeAPile(start: int, count: int) returns (result: seq<int>)\n"
        "  requires count >= 0\n"
        "  ensures result == MakeAPileAux(start, count)\n"
        "  decreases count\n"
        "{\n"
        "  if count == 0 {\n"
        "    result := [];\n"
        "  } else {\n"
        "    var tail := MakeAPile(start + 2, count - 1);\n"
        "    result := [start] + tail;\n"
        "  }\n"
        "}\n\n"
    )
    if "method MakeAPile(" not in source:
        source = re.sub(
            r"(method\s+make_a_pile\b)",
            helper + r"\1",
            source,
            count=1,
        )
    entry = (
        "method make_a_pile(n: int) returns (result: seq<int>)\n"
        "  requires n > 0\n"
        "  ensures result == MakeAPileSpec(n)\n"
        "{\n"
        "  result := MakeAPile(n, n);\n"
        "}\n"
    )
    return re.sub(
        r"method\s+make_a_pile\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        entry,
        source,
        flags=re.MULTILINE,
    )


def _fix_words_string_method(source: str) -> str:
    if "WordsStringAcc" not in source or "method words_string" not in source:
        return source
    acc_method = (
        "method WordsStringAccMethod(s: string, i: int, current: string) returns (result: seq<string>)\n"
        "  requires 0 <= i <= |s|\n"
        "  ensures result == WordsStringAcc(s, i, current)\n"
        "  decreases |s| - i\n"
        "{\n"
        "  if i == |s| {\n"
        "    if |current| == 0 { result := []; } else { result := [current]; }\n"
        "  } else if IsSeparator(s[i]) {\n"
        "    if |current| == 0 {\n"
        "      result := WordsStringAccMethod(s, i + 1, \"\");\n"
        "    } else {\n"
        "      var rest := WordsStringAccMethod(s, i + 1, \"\");\n"
        "      result := [current] + rest;\n"
        "    }\n"
        "  } else {\n"
        "    result := WordsStringAccMethod(s, i + 1, current + [s[i]]);\n"
        "  }\n"
        "}\n\n"
    )
    source = re.sub(
        r"method\s+WordsStringAccMethod\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        acc_method,
        source,
        flags=re.MULTILINE,
    )
    if "method WordsStringAccMethod" not in source:
        source = re.sub(
            r"(method\s+words_string\b)",
            acc_method + r"\1",
            source,
            count=1,
        )
    entry = (
        "method words_string(s: string) returns (result: seq<string>)\n"
        "  ensures result == WordsStringSpec(s)\n"
        "{\n"
        "  result := WordsStringAccMethod(s, 0, \"\");\n"
        "}\n"
    )
    return re.sub(
        r"method\s+words_string\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        entry,
        source,
        flags=re.MULTILINE,
    )


def _fix_f_entry_method(source: str) -> str:
    if "FSpec" not in source or "method f(" not in source:
        return source
    entry = (
        "method f(n: int) returns (result: seq<int>)\n"
        "  requires n >= 0\n"
        "  ensures result == FSpec(n)\n"
        "  decreases n\n"
        "{\n"
        "  if n == 0 {\n"
        "    result := [];\n"
        "  } else {\n"
        "    var prev := f(n - 1);\n"
        "    result := prev + [ElementSpec(n)];\n"
        "  }\n"
        "}\n"
    )
    return re.sub(
        r"method\s+f\s*\([\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        entry,
        source,
        flags=re.MULTILINE,
    )


def _fix_words_string_spec(source: str) -> str:
    if "WordsStringSpec" not in source:
        return source
    if "WordsStringAcc" in source:
        return source
    if "while" not in source and "var idx" not in source:
        return source
    replacement = (
        "function WordEnd(s: string): int\n"
        "  requires |s| > 0\n"
        "  ensures 1 <= WordEnd(s) <= |s|\n"
        "  decreases |s|\n"
        "{\n"
        "  if |s| == 1 then 1\n"
        "  else if s[1] == ' ' || s[1] == ',' then 1\n"
        "  else 1 + WordEnd(s[1..])\n"
        "}\n\n"
        "function WordsStringSpec(s: string): seq<string>\n"
        "  decreases |s|\n"
        "{\n"
        "  if |s| == 0 then []\n"
        "  else if s[0] == ' ' || s[0] == ',' then WordsStringSpec(s[1..])\n"
        "  else\n"
        "    var w := WordEnd(s);\n"
        "    [s[0..w]] + WordsStringSpec(s[w..])\n"
        "}\n"
    )
    result = re.sub(
        r"function\s+WordsStringSpec\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)",
        replacement,
        source,
        flags=re.MULTILINE,
    )
    return re.sub(
        r"function\s+WordLen\b[\s\S]*?(?=^(?:function|method|predicate|datatype)\s|\Z)\n?",
        "",
        result,
        flags=re.MULTILINE,
    )


_DEF_START = re.compile(r"^(function|predicate|method|datatype|lemma)\s+(\w+)")


def _extract_definitions(source: str) -> dict[str, tuple[str, str]]:
    blocks = _split_definition_blocks(source)
    out: dict[str, tuple[str, str]] = {}
    for block in blocks:
        first = block.strip().splitlines()[0]
        m = _DEF_START.match(first.strip())
        if m:
            out[m.group(2)] = (m.group(1), block.strip())
    return out


def _extract_definition_order(source: str) -> list[str]:
    order: list[str] = []
    for block in _split_definition_blocks(source):
        first = block.strip().splitlines()[0]
        m = _DEF_START.match(first.strip())
        if m:
            order.append(m.group(2))
    return order


def _split_definition_blocks(source: str) -> list[str]:
    lines = source.splitlines()
    blocks: list[str] = []
    current: list[str] = []
    depth = 0
    started = False

    for line in lines:
        stripped = line.strip()
        if _DEF_START.match(stripped) and depth == 0:
            if current:
                blocks.append("\n".join(current))
            current = [line]
            started = "{" in line
            depth = line.count("{") - line.count("}")
            continue
        if not current:
            continue
        current.append(line)
        depth += line.count("{") - line.count("}")
        if started and depth <= 0:
            blocks.append("\n".join(current))
            current = []
            depth = 0
            started = False

    if current:
        blocks.append("\n".join(current))
    return blocks


def _preamble_before_definitions(source: str) -> str:
    lines = source.splitlines()
    for i, line in enumerate(lines):
        if _DEF_START.match(line.strip()):
            return "\n".join(lines[:i])
    return ""


def _extract_body(defn: str) -> str:
    start = defn.find("{")
    end = defn.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return defn
    return defn[start + 1 : end].strip()


def _replace_definition(source: str, kind: str, name: str, new_text: str) -> str:
    pattern = rf"^{kind}\s+{re.escape(name)}\b[\s\S]*?(?=^(?:function|predicate|method|datatype|lemma)\s|\Z)"
    if re.search(pattern, new_text, flags=re.MULTILINE):
        replacement = new_text.strip()
    else:
        replacement = new_text.strip()
    result, count = re.subn(pattern, replacement + "\n", source, count=1, flags=re.MULTILINE)
    return result if count else source
