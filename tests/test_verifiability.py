from pathlib import Path

from vericode.models import CritiqueOutcome
from vericode.sources.github import ingest_pr
from vericode.sources.verifiability import assess_pr_verifiability


FIXTURES = Path(__file__).parent / "fixtures" / "pr"


def test_python_max_is_verifiable() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_max.json")
    assessment = assess_pr_verifiability(ctx)
    assert assessment.verifiable
    assert assessment.outcome is None


def test_posthog_error_response_not_verifiable() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "posthog_error_response.json")
    assessment = assess_pr_verifiability(ctx)
    assert not assessment.verifiable
    assert assessment.outcome == CritiqueOutcome.INHERENTLY_UNVERIFIABLE
    assert any("logging" in r.lower() or "Response" in r for r in assessment.reasons)


def test_async_python_not_verifiable() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "python_async_gap.json")
    assessment = assess_pr_verifiability(ctx)
    assert not assessment.verifiable
    assert assessment.outcome in (
        CritiqueOutcome.INHERENTLY_UNVERIFIABLE,
        CritiqueOutcome.TRANSLATION_GAP,
    )
