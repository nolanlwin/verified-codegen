"""Integration tests for Dafny verify/build without LLM."""

from __future__ import annotations

from pathlib import Path

import pytest

from vericode.dafny.toolchain import build_python, ensures_preserved, verify
from vericode.preflight import preflight


DOUBLE_DFY = """
method Double(n: int) returns (r: int)
  requires n >= 0
  ensures r == 2 * n
{
  r := n + n;
}
"""

DOUBLE_SKELETON = """
method Double(n: int) returns (r: int)
  requires n >= 0
  ensures r == 2 * n
{
  assume false;
}
"""


@pytest.mark.skipif(not preflight(require_openai=False, require_dafny=True).ok, reason="Dafny not installed")
def test_verify_and_build_double_example(tmp_path: Path) -> None:
    dfy = tmp_path / "double.dfy"
    dfy.write_text(DOUBLE_DFY, encoding="utf-8")

    verify_result = verify(dfy)
    assert verify_result.ok, verify_result.stderr

    output_dir = tmp_path / "out"
    build_result = build_python(dfy, output_dir)
    assert build_result.ok, build_result.stderr
    assert build_result.main_py is not None
    assert Path(build_result.main_py).exists()


def test_ensures_guard_on_double_example() -> None:
    assert ensures_preserved(DOUBLE_SKELETON, DOUBLE_DFY)
