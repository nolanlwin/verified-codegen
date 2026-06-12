from vericode.dafny.sanitize import (
    merge_skeleton_into_codegen,
    sanitize_dafny_implementation,
    sanitize_dafny_skeleton,
)
from vericode.dafny.toolchain import resolve, verify
from vericode.llm.codegen_agent import CodegenAgent


HAS_CLOSE_IMPL = """
function HasCloseElementsSpec(numbers: seq<real>, threshold: real): bool
  decreases |numbers|
{
  if |numbers| <= 1 then false
  else exists i, j :: 0 <= i < j < |numbers| && |numbers[i] - numbers[j]| < threshold
}

method HasCloseElements(numbers: seq<real>, threshold: real) returns (result: bool)
  requires threshold > 0.0
  ensures result == HasCloseElementsSpec(numbers, threshold)
{
  result := false;
}
"""

HAS_CLOSE_SKEL = """
function HasCloseElementsSpec(numbers: seq<real>, threshold: real): bool
  decreases |numbers|
{
  false
}

method HasCloseElements(numbers: seq<real>, threshold: real) returns (result: bool)
  requires threshold > 0.0
  ensures result == HasCloseElementsSpec(numbers, threshold)
{
  assume false;
}
"""


def test_implementation_fixes_real_abs() -> None:
    agent = CodegenAgent.__new__(CodegenAgent)
    out = agent.prepare_source(HAS_CLOSE_SKEL, HAS_CLOSE_IMPL)
    assert "AbsDistReal" in out
    assert "|numbers[i] - numbers[j]|" not in out
    assert resolve.__module__  # noqa: B018 — keep import used


def test_merge_preserves_non_stub_spec() -> None:
    skel = sanitize_dafny_skeleton(
        """
function WordsStringSpec(s: string): seq<string>
  decreases |s|
{
  if |s| == 0 then []
  else if s[0] == ' ' then WordsStringSpec(s[1..])
  else [""] + WordsStringSpec(s[1..])
}

method WordsString(s: string) returns (result: seq<string>)
  ensures result == WordsStringSpec(s)
{
  assume false;
}
"""
    )
    gen = """
function WordsStringSpec(s: string): seq<string> { while true { } [] }
method WordsString(s: string) returns (result: seq<string>)
  ensures result == WordsStringSpec(s)
{ result := []; }
"""
    merged = merge_skeleton_into_codegen(skel, gen)
    assert "while" not in merged.split("method")[0]


def test_make_apile_spec_and_impl_repair() -> None:
    raw = """
function MakeAPileSpec(n: int): seq<int>
  decreases n
{
  if n == 1 then [n]
  else [n] + MakeAPileSpec(n + 1)
}

method MakeAPile(n: int) returns (result: seq<int>)
  requires n > 0
  ensures result == MakeAPileSpec(n)
{
  assume false;
}
"""
    skel = sanitize_dafny_skeleton(raw)
    impl = sanitize_dafny_implementation(
        """
function MakeAPileSpec(n: int): seq<int>
  decreases n
{ if n == 1 then [n] else MakeAPileSpec(n - 1) + [n + 2 * (n - 1)] }

method MakeAPile(n: int) returns (result: seq<int>)
  requires n > 0
  ensures result == MakeAPileSpec(n)
  decreases n
{
  if n == 1 { result := [n]; }
  else { var sub := MakeAPile(n + 1); result := [n] + sub; }
}
"""
    )
    agent = CodegenAgent.__new__(CodegenAgent)
    out = agent.prepare_source(skel, impl)
    assert "MakeAPileAux" in out
    assert "MakeAPile(n, n)" in out or "MakeAPile(start + 2, count - 1)" in out
    assert "MakeAPile(n + 1)" not in out
