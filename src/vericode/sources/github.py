from __future__ import annotations

import json
import re
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

from vericode.models import FileChange, ReviewComment, TaskContext
from vericode.sources.context import (
    build_task_context_from_fixture,
    detect_language,
    extract_scoped_symbol,
    list_translatable_symbols,
)


_PR_URL_RE = re.compile(
    r"^https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/pull/(?P<number>\d+)/?$"
)


def parse_pr_url(url: str) -> tuple[str, str, int]:
    match = _PR_URL_RE.match(url.strip())
    if not match:
        raise ValueError(f"Not a GitHub pull request URL: {url}")
    owner = match.group("owner")
    repo = match.group("repo")
    number = int(match.group("number"))
    return f"{owner}/{repo}", repo, number


def _run_gh(args: list[str]) -> str:
    try:
        proc = subprocess.run(
            ["gh", *args],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("GitHub CLI `gh` not found. Install gh or use --fixture.") from exc
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "gh command failed")
    return proc.stdout


def fetch_pr_via_gh(url: str) -> TaskContext:
    repo_slug, _, number = parse_pr_url(url)
    owner, repo = repo_slug.split("/", 1)

    pr_json = json.loads(
        _run_gh(["api", f"repos/{owner}/{repo}/pulls/{number}"])
    )
    files_raw = json.loads(
        _run_gh(["api", f"repos/{owner}/{repo}/pulls/{number}/files", "--paginate"])
    )
    issue_comments = json.loads(
        _run_gh(["api", f"repos/{owner}/{repo}/issues/{number}/comments", "--paginate"])
    )
    review_comments = json.loads(
        _run_gh(["api", f"repos/{owner}/{repo}/pulls/{number}/comments", "--paginate"])
    )

    files: list[FileChange] = []
    for item in files_raw:
        path = item.get("filename", "")
        patch = item.get("patch") or ""
        files.append(
            FileChange(
                path=path,
                language=detect_language(path),
                patch=patch,
                before="",
                after=_apply_patch_placeholder(patch),
                status=item.get("status", "modified"),
            )
        )

    head_sha = pr_json.get("head", {}).get("sha", "")
    head_ref = pr_json.get("head", {}).get("ref", head_sha)
    for fc in files:
        if fc.language not in ("python", "typescript", "javascript"):
            continue
        full_source = _fetch_file_at_ref(owner, repo, fc.path, head_sha, head_ref)
        if full_source:
            fc.after = full_source

    comments = [
        ReviewComment(author=c.get("user", {}).get("login", ""), body=c.get("body", ""))
        for c in issue_comments
    ]
    rev_comments = [
        ReviewComment(
            author=c.get("user", {}).get("login", ""),
            body=c.get("body", ""),
            path=c.get("path"),
            line=c.get("line") or c.get("original_line"),
        )
        for c in review_comments
    ]

    data: dict[str, Any] = {
        "repo": repo_slug,
        "pr": {
            "number": number,
            "title": pr_json.get("title", ""),
            "body": pr_json.get("body") or "",
            "author": pr_json.get("user", {}).get("login", ""),
            "url": pr_json.get("html_url", url),
            "base_sha": pr_json.get("base", {}).get("sha", ""),
            "head_sha": pr_json.get("head", {}).get("sha", ""),
        },
        "files": [f.model_dump() for f in files],
        "comments": [c.model_dump() for c in comments],
        "review_comments": [c.model_dump() for c in rev_comments],
    }
    return build_task_context_from_fixture(data)


def _fetch_file_at_ref(
    owner: str,
    repo: str,
    path: str,
    head_sha: str,
    head_ref: str,
) -> str:
    """Fetch full file text at PR head; fall back to raw.githubusercontent.com."""
    if head_sha:
        try:
            content = _run_gh(
                [
                    "api",
                    f"repos/{owner}/{repo}/contents/{path}",
                    "-f",
                    f"ref={head_sha}",
                ]
            )
            blob = json.loads(content)
            if blob.get("encoding") == "base64":
                import base64

                return base64.b64decode(blob["content"]).decode("utf-8", errors="replace")
        except (RuntimeError, json.JSONDecodeError, KeyError):
            pass

    for ref in (head_ref, head_sha):
        if not ref:
            continue
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/{quote(ref, safe='/')}/{path}"
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:  # noqa: S310
                return resp.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError):
            continue
    return ""


def _apply_patch_placeholder(patch: str) -> str:
    """Best-effort reconstruction of post-image lines from unified diff hunks."""
    if not patch.strip():
        return ""
    lines: list[str] = []
    for line in patch.splitlines():
        if line.startswith("+++") or line.startswith("---") or line.startswith("@@"):
            continue
        if line.startswith("+"):
            lines.append(line[1:])
    return "\n".join(lines)


def ingest_pr(
    *,
    url: str | None = None,
    fixture: Path | None = None,
    focus: str | None = None,
    patch_file: Path | None = None,
    meta_file: Path | None = None,
) -> TaskContext:
    if fixture is not None:
        data = json.loads(fixture.read_text(encoding="utf-8"))
        if focus:
            data["focus"] = focus
        ctx = build_task_context_from_fixture(data, focus=focus or data.get("focus"))
    elif patch_file is not None:
        patch = patch_file.read_text(encoding="utf-8")
        meta: dict[str, Any] = {}
        if meta_file and meta_file.is_file():
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
        path = meta.get("path", "source.py")
        data = {
            "repo": meta.get("repo", "local/fixture"),
            "pr": {
                "number": meta.get("number", 0),
                "title": meta.get("title", "Local patch"),
                "body": meta.get("body", ""),
                "author": meta.get("author", "local"),
                "url": meta.get("url", ""),
            },
            "files": [{"path": path, "language": detect_language(path), "patch": patch, "after": _apply_patch_placeholder(patch)}],
            "comments": meta.get("comments", []),
            "review_comments": meta.get("review_comments", []),
            "focus": focus or meta.get("focus"),
        }
        ctx = build_task_context_from_fixture(data, focus=data.get("focus"))
    elif url:
        ctx = fetch_pr_via_gh(url)
        if focus:
            ctx.focus = extract_scoped_symbol(ctx, focus)
            ctx.verification_scope = f"{ctx.focus.path}:{ctx.focus.name}"
    else:
        raise ValueError("Provide pr_url, --fixture, or --patch")

    if focus and ctx.focus is None:
        ctx.focus = extract_scoped_symbol(ctx, focus)
        ctx.verification_scope = f"{ctx.focus.path}:{ctx.focus.name}"

    if ctx.focus is None:
        symbols = list_translatable_symbols(ctx)
        if len(symbols) == 1:
            path, name, lang = symbols[0]
            ctx.focus = extract_scoped_symbol(ctx, f"{path}:{name}")
            ctx.verification_scope = f"{path}:{name}"

    return ctx


def is_github_pr_url(value: str) -> bool:
    try:
        parse_pr_url(value)
        return True
    except ValueError:
        return bool(urlparse(value).netloc == "github.com" and "/pull/" in value)
