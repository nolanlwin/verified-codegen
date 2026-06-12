from pathlib import Path

import pytest

from vericode.artifacts.store import SessionStore
from vericode.models import CritiqueOutcome
from vericode.sources.context import (
    extract_scoped_symbol,
    feasibility_precheck,
    list_translatable_symbols,
    render_pr_prompt,
)
from vericode.sources.github import ingest_pr, parse_pr_url


FIXTURES = Path(__file__).parent / "fixtures" / "pr"


def test_parse_pr_url() -> None:
    repo, name, num = parse_pr_url("https://github.com/org/repo/pull/123")
    assert repo == "org/repo"
    assert name == "repo"
    assert num == 123


def test_ingest_python_fixture() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    assert ctx.pr_number == 42
    assert ctx.focus is not None
    assert ctx.focus.name == "max_of_two"
    assert ctx.focus.language == "python"
    assert "max_of_two" in ctx.focus.source


def test_ingest_typescript_fixture() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "typescript_sum.json")
    assert ctx.focus is not None
    assert ctx.focus.language == "typescript"
    assert "sumArray" in ctx.focus.source


def test_list_translatable_symbols_mixed() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    symbols = list_translatable_symbols(ctx)
    assert ("src/math_utils.py", "max_of_two", "python") in symbols


def test_render_pr_prompt_includes_conflict_hints() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    prompt = render_pr_prompt(ctx)
    assert "max_of_two" in prompt
    assert "Review comment" in prompt or "reviewer" in prompt


def test_feasibility_rejects_async_python() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_async_gap.json")
    ok, message, outcome = feasibility_precheck(ctx)
    assert not ok
    assert outcome in (CritiqueOutcome.TRANSLATION_GAP, CritiqueOutcome.INHERENTLY_UNVERIFIABLE)
    assert "async" in message.lower() or "import" in message.lower()


def test_create_pr_session_writes_context(tmp_path: Path) -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    store = SessionStore(root=tmp_path / "sessions")
    meta = store.create_pr_session(ctx, render_pr_prompt(ctx))
    assert meta.source_type == "github_pr"
    assert meta.verification_mode == "verify_pr"
    assert meta.focus_symbol == "src/math_utils.py:max_of_two"
    loaded = store.read_context(meta.session_id)
    assert loaded.focus is not None
    assert loaded.focus.name == "max_of_two"


def test_extract_scoped_symbol_requires_focus() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    sym = extract_scoped_symbol(ctx, "src/math_utils.py:max_of_two")
    assert sym.start_line >= 1
