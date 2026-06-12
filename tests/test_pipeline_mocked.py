"""Pipeline smoke test with mocked LLM responses (no OpenAI required)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from vericode.artifacts.store import SessionStore
from vericode.llm.codegen_agent import CodegenAgent
from vericode.llm.spec_agent import SpecAgent
from vericode.models import SessionStatus, SpecAgentResponse
from vericode.pipeline import Pipeline
from vericode.preflight import PreflightResult, preflight


SKELETON = """
function DoubleSpec(n: int): int
  requires n >= 0
{
  2 * n
}

method Double(n: int) returns (r: int)
  requires n >= 0
  ensures r == DoubleSpec(n)
{
  assume false;
}
"""

IMPLEMENTATION = """
function DoubleSpec(n: int): int
  requires n >= 0
{
  2 * n
}

method Double(n: int) returns (r: int)
  requires n >= 0
  ensures r == DoubleSpec(n)
{
  r := n + n;
}
"""

NL_SPEC = """
Double a non-negative integer.

Preconditions:
- Input is a non-negative integer.

Postconditions:
- Output equals twice the input.
"""


@pytest.mark.skipif(not preflight(require_openai=False, require_dafny=True).ok, reason="Dafny not installed")
def test_pipeline_with_mocked_llm(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    store = SessionStore(root=tmp_path / "sessions")
    pipeline = Pipeline(store=store)

    spec_response = SpecAgentResponse(
        internal_dafny=SKELETON,
        nl_summary=NL_SPEC,
        notes=[],
    )

    ok = PreflightResult(ok=True, dafny_path="dafny", openai_configured=True)
    with patch("vericode.pipeline.preflight", return_value=ok), patch.object(
        SpecAgent, "generate", return_value=spec_response
    ), patch.object(
        SpecAgent, "repair", return_value=spec_response
    ), patch.object(
        CodegenAgent, "generate", return_value=IMPLEMENTATION
    ), patch.object(
        CodegenAgent, "fix", return_value=IMPLEMENTATION
    ):
        session_id = pipeline.new_session(
            "Double a non-negative integer.",
            auto_approve=True,
        )

    meta = store.read_meta(session_id)
    assert meta.status == SessionStatus.DONE
    assert meta.verified
    assert (store.session_dir(session_id) / "final.py").exists()
