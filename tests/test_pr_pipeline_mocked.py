from pathlib import Path
from unittest.mock import MagicMock, patch

from vericode.artifacts.store import SessionStore
from vericode.llm.spec_agent import SpecAgent
from vericode.models import SessionStatus, SpecAgentResponse
from vericode.pipeline import Pipeline
from vericode.review.interactive import ReviewAction
from vericode.sources.github import ingest_pr


FIXTURES = Path(__file__).parent / "fixtures" / "pr"


def test_pr_session_spec_generation_mocked(tmp_path: Path) -> None:
    store = SessionStore(root=tmp_path / "sessions")
    pipeline = Pipeline(store=store, console=MagicMock())

    skeleton = """
function MaxSpec(a: int, b: int): int { if a >= b then a else b }
method MaxOfTwo(a: int, b: int) returns (r: int)
  ensures r == MaxSpec(a, b)
{ assume false; }
"""
    response = SpecAgentResponse(
        internal_dafny=skeleton,
        nl_summary="Return the larger of two integers.",
        notes=["Comment requests equal-input handling."],
    )

    with patch("vericode.pipeline.preflight") as mock_pf:
        mock_pf.return_value.ok = True
        mock_pf.return_value.errors = []
        with patch("vericode.pipeline.OpenAIClient"):
            with patch("vericode.pipeline.SpecAgent") as mock_agent_cls:
                mock_agent_cls.prepare_dafny_static = staticmethod(SpecAgent.prepare_dafny_static)
                agent = mock_agent_cls.return_value
                agent.generate_from_pr.return_value = response
                agent.format_draft_spec.side_effect = SpecAgent.format_draft_spec
                with patch.object(pipeline, "_verify_spec_skeleton") as mock_resolve:
                    mock_resolve.return_value = MagicMock(ok=True, stdout="", stderr="")
                    with patch.object(
                        pipeline,
                        "review_session",
                        return_value=(ReviewAction.ABORT, None),
                    ):
                        with patch.object(pipeline, "_save_critique_abort"):
                            session_id = pipeline.new_pr_session(
                                fixture=FIXTURES / "python_max.json",
                                skip_run=True,
                            )

    meta = store.read_meta(session_id)
    assert meta.source_type == "github_pr"
    assert meta.verification_mode == "verify_pr"
    assert store.read_text(session_id, "draft_spec.md").startswith("Return the larger")
    assert meta.status in (SessionStatus.AWAITING_REVIEW, SessionStatus.FAILED, SessionStatus.DONE_WITH_FINDINGS)
