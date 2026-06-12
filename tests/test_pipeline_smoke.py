from pathlib import Path

import pytest

from vericode.artifacts.store import SessionStore
from vericode.dafny.toolchain import ensures_preserved, extract_ensures_clauses, verify
from vericode.models import SessionStatus
from vericode.preflight import preflight


def test_session_store_create_and_list(tmp_path: Path) -> None:
    store = SessionStore(root=tmp_path / "sessions")
    meta = store.create_session("sort a list")
    assert meta.session_id
    assert store.read_text(meta.session_id, "prompt.txt") == "sort a list"

    store.write_text(meta.session_id, "draft_spec.md", "draft")
    store.copy_verified_spec(meta.session_id)
    assert store.read_text(meta.session_id, "verified_spec.md") == "draft"

    listed = store.list_sessions()
    assert len(listed) == 1
    assert listed[0].session_id == meta.session_id


def test_ensures_preserved_detects_weakening() -> None:
    skeleton = """
method M(x: int) returns (r: int)
  ensures r >= 0
  ensures r == x + 1
{ ... }
"""
    good = """
method M(x: int) returns (r: int)
  ensures r >= 0
  ensures r == x + 1
{ r := x + 1; }
"""
    bad = """
method M(x: int) returns (r: int)
  ensures r >= 0
{ r := x + 1; }
"""
    assert ensures_preserved(skeleton, good)
    assert not ensures_preserved(skeleton, bad)


def test_extract_ensures_clauses() -> None:
    source = "method M() ensures x > 0 ensures y == 1 { }"
    clauses = extract_ensures_clauses(source)
    assert "x > 0" in clauses
    assert "y == 1" in clauses


@pytest.mark.skipif(not preflight(require_openai=False, require_dafny=True).ok, reason="Dafny not installed")
def test_verify_handwritten_spec(tmp_path: Path) -> None:
    dfy = tmp_path / "spec.dfy"
    dfy.write_text(
        """
function Id(n: int): int { n }

method Compute(n: int) returns (r: int)
  ensures r == Id(n)
{
  assume false;
}
""",
        encoding="utf-8",
    )
    result = verify(dfy, allow_warnings=True)
    assert result.ok, result.stderr
