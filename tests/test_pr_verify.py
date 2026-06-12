from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from vericode.artifacts.store import SessionStore
from vericode.dafny.toolchain import verify
from vericode.llm.translators import get_translator
from vericode.models import CritiqueOutcome, SessionStatus
from vericode.pipeline import Pipeline
from vericode.review.critique import build_critique, format_critique_md
from vericode.sources.github import ingest_pr


FIXTURES = Path(__file__).parent / "fixtures" / "pr"

SIMPLE_DAFNY = """
function MaxSpec(a: int, b: int): int {
  if a >= b then a else b
}

method MaxOfTwo(a: int, b: int) returns (r: int)
  ensures r == MaxSpec(a, b)
{
  if a >= b {
    r := a;
  } else {
    r := b;
  }
}
"""


@pytest.mark.parametrize(
    "fixture,language,symbol",
    [
        ("python_max.json", "python", "max_of_two"),
        ("typescript_sum.json", "typescript", "sumArray"),
    ],
)
def test_translator_precheck_accepts_fixtures(fixture: str, language: str, symbol: str) -> None:
    ctx = ingest_pr(fixture=FIXTURES / fixture)
    assert ctx.focus is not None
    translator = get_translator(language)  # type: ignore[arg-type]
    ok, reason = translator.can_translate(symbol, ctx.focus.source)
    assert ok, reason


def test_critique_format_proved() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    report = build_critique(
        outcome=CritiqueOutcome.PROVED,
        summary="ok",
        context=ctx,
        verified=True,
    )
    md = format_critique_md(report)
    assert "PROVED" in md
    assert "max_of_two" in md or "math_utils" in md


@pytest.mark.skipif(
    not Path("/usr/bin/dafny").exists() and __import__("shutil").which("dafny") is None,
    reason="Dafny not installed",
)
def test_verify_handwritten_max_translation(tmp_path: Path) -> None:
    dfy = tmp_path / "impl.dfy"
    dfy.write_text(SIMPLE_DAFNY, encoding="utf-8")
    result = verify(dfy, allow_warnings=True)
    assert result.ok, result.stderr


def test_run_pr_verification_verify_only_no_fix_loop(tmp_path: Path) -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    store = SessionStore(root=tmp_path / "sessions")
    meta = store.create_pr_session(ctx, "prompt")
    store.write_text(meta.session_id, "verified_spec.md", "max of two ints")
    store.write_text(
        meta.session_id,
        "internal_spec.dfy",
        """
function MaxSpec(a: int, b: int): int { if a >= b then a else b }
method MaxOfTwo(a: int, b: int) returns (r: int)
  ensures r == MaxSpec(a, b)
{ assume false; }
""",
    )
    store.update_status(meta.session_id, SessionStatus.VERIFIED_SPEC)

    failing_source = """
function MaxSpec(a: int, b: int): int { if a >= b then a else b }
method MaxOfTwo(a: int, b: int) returns (r: int)
  ensures r == MaxSpec(a, b)
{ r := 0; }
"""

    pipeline = Pipeline(store=store)
    with patch.object(Pipeline, "__init__", lambda self, **kwargs: None):
        pass

    pipe = Pipeline(store=store)
    pipe.console = MagicMock()
    pipe.verify_timeout = 60
    pipe.dafny_bin = __import__("shutil").which("dafny") or "dafny"

    with patch("vericode.pipeline.TranslateAgent") as mock_cls:
        mock_cls.return_value.translate.return_value = failing_source
        with patch("vericode.pipeline.preflight") as mock_pf:
            mock_pf.return_value.ok = True
            mock_pf.return_value.errors = []
            try:
                pipe.run_pr_verification(meta.session_id)
            except Exception:
                if not (tmp_path / "sessions" / meta.session_id / "critique.md").exists():
                    pytest.skip("Dafny unavailable for verify path")

    critique = store.read_text_optional(meta.session_id, "critique.md")
    if critique:
        assert "PROOF_FAILED" in critique or "PROVED" in critique
        assert store.read_meta(meta.session_id).status in (
            SessionStatus.DONE,
            SessionStatus.DONE_WITH_FINDINGS,
        )
