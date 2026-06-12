from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from vericode.models import FileChange, ReviewComment, ScopedSymbol, SourceLanguage, TaskContext


_LANGUAGE_BY_EXT: dict[str, SourceLanguage] = {
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
}


def detect_language(path: str) -> SourceLanguage:
    ext = Path(path).suffix.lower()
    return _LANGUAGE_BY_EXT.get(ext, "unknown")


def _classify_pr_shape(files: list[FileChange]) -> str:
    langs = {f.language for f in files if f.language != "unknown"}
    if not langs:
        return "unknown"
    if langs <= {"python", "typescript", "javascript"}:
        code_files = [f for f in files if f.language in ("python", "typescript", "javascript")]
        if len(code_files) == 1 and not any(c in f.after for f in code_files for c in ("def ", "function ", "=>")):
            return "config_only"
        combined = "\n".join(f.patch + f.after for f in code_files)
        if re.search(r"\blogger\.(warning|info|error|debug)\b", combined):
            return "observability"
        if re.search(r"@api_view|HttpResponse|->\s*Response\b", combined):
            return "web_framework"
        return "pure_function"
    return "mixed_unsupported"


def build_task_context_from_fixture(data: dict[str, Any], *, focus: str | None = None) -> TaskContext:
    pr = data.get("pr", {})
    files: list[FileChange] = []
    for item in data.get("files", []):
        path = item["path"]
        files.append(
            FileChange(
                path=path,
                language=item.get("language") or detect_language(path),
                patch=item.get("patch", ""),
                before=item.get("before", ""),
                after=item.get("after", ""),
                status=item.get("status", "modified"),
            )
        )

    comments = [ReviewComment(**c) for c in data.get("comments", [])]
    review_comments = [ReviewComment(**c) for c in data.get("review_comments", [])]

    ctx = TaskContext(
        repo=data.get("repo", pr.get("repo", "")),
        pr_number=int(pr.get("number", 0)),
        title=pr.get("title", ""),
        body=pr.get("body", ""),
        author=pr.get("author", ""),
        url=pr.get("url", ""),
        base_sha=pr.get("base_sha", ""),
        head_sha=pr.get("head_sha", ""),
        files=files,
        comments=comments,
        review_comments=review_comments,
        pr_shape=_classify_pr_shape(files),
    )

    if focus:
        scoped = extract_scoped_symbol(ctx, focus)
        ctx.focus = scoped
        ctx.verification_scope = f"{scoped.path}:{scoped.name}"
    return ctx


def load_fixture(path: Path) -> TaskContext:
    data = json.loads(path.read_text(encoding="utf-8"))
    focus = data.get("focus")
    return build_task_context_from_fixture(data, focus=focus)


def parse_focus(focus: str) -> tuple[str, str]:
    if ":" not in focus:
        raise ValueError(f"Focus must be path:symbol, got {focus!r}")
    path, symbol = focus.rsplit(":", 1)
    return path.strip(), symbol.strip()


def list_translatable_symbols(ctx: TaskContext) -> list[tuple[str, str, SourceLanguage]]:
    symbols: list[tuple[str, str, SourceLanguage]] = []
    for fc in ctx.files:
        if fc.language not in ("python", "typescript", "javascript"):
            continue
        for name in _list_symbols_in_source(fc.after or fc.patch, fc.language):
            symbols.append((fc.path, name, fc.language))
    return symbols


def _list_symbols_in_source(source: str, language: SourceLanguage) -> list[str]:
    names: list[str] = []
    if language == "python":
        for match in re.finditer(r"^\s*def\s+(\w+)\s*\(", source, re.MULTILINE):
            names.append(match.group(1))
    else:
        for match in re.finditer(r"^\s*(?:export\s+)?function\s+(\w+)\s*\(", source, re.MULTILINE):
            names.append(match.group(1))
        for match in re.finditer(r"^\s*(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s*)?\(", source, re.MULTILINE):
            names.append(match.group(1))
        for match in re.finditer(r"^\s*(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s*)?[^=]*=>", source, re.MULTILINE):
            if match.group(1) not in names:
                names.append(match.group(1))
    return names


def extract_scoped_symbol(ctx: TaskContext, focus: str) -> ScopedSymbol:
    path, name = parse_focus(focus)
    fc = next((f for f in ctx.files if f.path == path or f.path.endswith("/" + path)), None)
    if fc is None:
        fc = next((f for f in ctx.files if Path(f.path).name == Path(path).name), None)
    if fc is None:
        raise ValueError(f"File not found in PR changes: {path}")

    source = fc.after or fc.before
    language = fc.language if fc.language != "unknown" else detect_language(path)
    if language not in ("python", "typescript", "javascript"):
        raise ValueError(f"Unsupported language for focus: {language}")

    snippet, start_line = _extract_symbol_snippet(source, name, language)
    if not snippet:
        raise ValueError(f"Symbol {name!r} not found in {path}")

    return ScopedSymbol(
        path=fc.path,
        name=name,
        language=language,
        kind="method" if language == "python" and snippet.lstrip().startswith("def ") and "self" in snippet.split("(")[0] else "function",
        source=snippet,
        start_line=start_line,
    )


def _extract_symbol_snippet(source: str, name: str, language: SourceLanguage) -> tuple[str, int]:
    lines = source.splitlines()
    if language == "python":
        pattern = re.compile(rf"^(\s*)(?:async\s+)?def\s+{re.escape(name)}\s*\(")
    else:
        pattern = re.compile(
            rf"^(\s*)(?:export\s+)?(?:function\s+{re.escape(name)}\s*\(|const\s+{re.escape(name)}\s*=)"
        )

    start_idx: int | None = None
    indent = ""
    for i, line in enumerate(lines):
        m = pattern.match(line)
        if m:
            start_idx = i
            indent = m.group(1)
            break

    if start_idx is None:
        return "", 1

    end_idx = start_idx + 1
    while end_idx < len(lines):
        line = lines[end_idx]
        if not line.strip():
            end_idx += 1
            continue
        if language == "python":
            if _python_symbol_boundary(line, indent):
                break
        elif not line[0].isspace():
            break
        end_idx += 1

    snippet = "\n".join(lines[start_idx:end_idx])
    return snippet, start_idx + 1


def _python_symbol_boundary(line: str, indent: str) -> bool:
    """True when line starts the next Python definition at the same scope."""
    if indent:
        if line.startswith(indent + " ") or line.startswith(indent + "\t"):
            return False
        if not line.startswith(indent):
            return False
        rest = line[len(indent) :]
    else:
        if line[:1].isspace():
            return False
        rest = line
    return bool(re.match(r"^(?:async\s+)?def\s+\w+\s*\(|^class\s+\w+", rest))


def render_pr_prompt(ctx: TaskContext, *, symbol_context_block: str = "") -> str:
    parts = [
        f"GitHub PR #{ctx.pr_number}: {ctx.title}",
        f"Author: {ctx.author}",
        f"URL: {ctx.url}",
    ]
    if ctx.body.strip():
        parts.append(f"PR description:\n{ctx.body.strip()}")

    if ctx.focus:
        parts.append(
            f"Verification focus: {ctx.focus.path}:{ctx.focus.name} ({ctx.focus.language})\n"
            f"Scoped source:\n```{ctx.focus.language}\n{ctx.focus.source}\n```"
        )

    for fc in ctx.files:
        if ctx.focus and fc.path == ctx.focus.path:
            continue
        parts.append(f"Changed file: {fc.path} ({fc.language})")
        if fc.patch.strip():
            parts.append(f"Diff hunk:\n{fc.patch.strip()}")

    for group, label in ((ctx.comments, "PR comment"), (ctx.review_comments, "Review comment")):
        for c in group:
            loc = f" on {c.path}:{c.line}" if c.path else ""
            parts.append(f"{label}{loc} (@{c.author}): {c.body}")

    if ctx.scope_notes:
        parts.append("Scope notes:\n" + "\n".join(f"- {n}" for n in ctx.scope_notes))

    if symbol_context_block.strip():
        parts.append(symbol_context_block.strip())

    return "\n\n".join(parts)


def feasibility_precheck(ctx: TaskContext) -> tuple[bool, str, CritiqueOutcome | None]:
    from vericode.models import CritiqueOutcome

    if ctx.pr_shape == "config_only":
        return False, "PR contains only config/non-algorithmic changes.", CritiqueOutcome.OUT_OF_SCOPE

    if ctx.focus is None:
        return False, "No focus symbol selected. Use --focus path:symbol.", CritiqueOutcome.OUT_OF_SCOPE

    if ctx.focus.language not in ("python", "typescript", "javascript"):
        syms = list_translatable_symbols(ctx)
        hint = ", ".join(f"{p}:{n}" for p, n, _ in syms[:8]) or "(none found)"
        return False, f"Unsupported focus language. Translatable symbols: {hint}", CritiqueOutcome.OUT_OF_SCOPE

    from vericode.llm.translators import get_translator

    translator = get_translator(ctx.focus.language)
    ok, reason = translator.can_translate(ctx.focus.name, ctx.focus.source)
    if not ok:
        outcome = (
            CritiqueOutcome.INHERENTLY_UNVERIFIABLE
            if "async" in reason.lower() or "import" in reason.lower()
            else CritiqueOutcome.TRANSLATION_GAP
        )
        return False, reason, outcome

    return True, "", None
