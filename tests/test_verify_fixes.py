from pathlib import Path

import pytest

from vericode.dafny.toolchain import verify
from vericode.llm.codegen_agent import CodegenAgent


@pytest.mark.parametrize(
    "session_id",
    ["b450eee5e525", "94335d92bdcd", "473cd47ac97c"],
)
def test_repair_known_verify_failures(session_id: str, tmp_path: Path) -> None:
    base = Path(__file__).resolve().parents[1] / ".vericode" / "bench" / "humaneval" / "sessions"
    session = base / session_id
    if not (session / "implementation.dfy").is_file():
        pytest.skip("benchmark session not available")

    agent = CodegenAgent.__new__(CodegenAgent)
    fixed = agent.prepare_source(
        (session / "internal_spec.dfy").read_text(),
        (session / "implementation.dfy").read_text(),
    )
    out = tmp_path / f"{session_id}.dfy"
    out.write_text(fixed)
    result = verify(out, allow_warnings=True)
    assert result.ok, result.stderr[:500]
