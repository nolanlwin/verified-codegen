import re

from vericode.dafny.sanitize import (
    repair_hints,
    sanitize_dafny_implementation,
    sanitize_dafny_skeleton,
    _fix_method_if_then_else,
    _fix_python_single_quoted_strings,
    _strip_function_ensures,
    _fix_function_body_semicolons,
)
from vericode.dafny.toolchain import resolve, verify

HAS_CLOSE = """
function HasCloseElementsSpec(numbers: seq<real>, threshold: real): bool
  requires |numbers| > 1
  ensures HasCloseElementsSpec(numbers, threshold) == (exists i, j: int :: 0 <= i < j < |numbers|)
{
  if |numbers| == 2 then true else false
}

method HasCloseElements(numbers: seq<real>, threshold: real) returns (result: bool)
  requires |numbers| > 1
  ensures result == HasCloseElementsSpec(numbers, threshold)
{
  assume false;
}
"""

WHILE_FUNCTION = """
function SeparateParenGroupsSpec(paren_string: string): seq<string>
{
  var cleaned := paren_string;
  while true
  {
    cleaned := cleaned;
  }
  []
}

method SeparateParenGroups(paren_string: string) returns (result: seq<string>)
  ensures result == SeparateParenGroupsSpec(paren_string)
{
  assume false;
}
"""

MISSING_SEMICOLON = """
function ComputeFactorialsAndSums(n: int): seq<int>
  requires n >= 0
{
  if n == 0 then []
  else
    var tail := ComputeFactorialsAndSums(n - 1)
    var current := if n % 2 == 0 then 1 else 1
    [current] + tail
}

method F(n: int) returns (result: seq<int>)
  ensures result == ComputeFactorialsAndSums(n)
{
  assume false;
}
"""


def test_strip_function_ensures() -> None:
    out = _strip_function_ensures(HAS_CLOSE)
    assert "ensures HasCloseElementsSpec" not in out.split("method")[0]
    assert "ensures result ==" in out


def test_stub_imperative_function() -> None:
    out = sanitize_dafny_skeleton(WHILE_FUNCTION)
    assert "while" not in out
    assert "SeparateParenGroupsSpec" in out


def test_fix_function_body_semicolons() -> None:
    out = _fix_function_body_semicolons(MISSING_SEMICOLON)
    assert "var tail := ComputeFactorialsAndSums(n - 1);" in out


def test_sanitize_full_pipeline() -> None:
    out = sanitize_dafny_skeleton(MISSING_SEMICOLON)
    assert "var tail :=" in out
    assert ";" in out.split("var tail")[1][:40]


def test_fix_method_if_then_else() -> None:
    raw = """
method M(x: bool) returns (result: seq<string>)
  ensures true
{
  if x then
    result := ["a"];
  else
    result := [];
}
"""
    out = _fix_method_if_then_else(raw)
    assert "if x then" not in out
    assert "if x {" in out
    assert "} else {" in out


def test_strip_bare_decreases_allows_verify() -> None:
    from pathlib import Path

    impl = Path(".vericode/sessions/05d94c71098b/implementation.dfy")
    if not impl.is_file():
        return
    fixed = sanitize_dafny_implementation(impl.read_text(), skip_benchmark_injection=True)
    assert re.search(r"^\s*decreases\s*$", fixed, re.MULTILINE) is None
    tmp = Path("/tmp/05d94_impl.dfy")
    tmp.write_text(fixed)
    result = verify(tmp, allow_warnings=True)
    assert result.ok, result.stderr


def test_session_fc615_translation_sanitizes_and_verifies() -> None:
    from pathlib import Path

    impl = Path(".vericode/sessions/fc615c8e481b/implementation.dfy")
    if not impl.is_file():
        return
    fixed = sanitize_dafny_implementation(impl.read_text(), skip_benchmark_injection=True)
    assert "if has_slack_thread_context {" in fixed
    tmp = Path("/tmp/fc615_impl.dfy")
    tmp.write_text(fixed)
    result = verify(tmp, allow_warnings=True)
    assert result.ok, result.stderr


def test_fix_python_single_quoted_strings() -> None:
    raw = "if x then ['slack_response_style'] else []"
    out = _fix_python_single_quoted_strings(raw)
    assert out == 'if x then ["slack_response_style"] else []'


def test_repair_hints_for_unary() -> None:
    hints = repair_hints("invalid UnaryExpression", "abs(x)")
    assert "abs" in hints.lower() or "unary" in hints.lower()


def test_sanitize_benchmark_sessions_resolve() -> None:
    from pathlib import Path

    base = Path(__file__).resolve().parents[1] / ".vericode" / "bench" / "humaneval" / "sessions"
    if not base.is_dir():
        return
    specs = list(base.glob("*/internal_spec.dfy"))
    if not specs:
        return
    tmp = Path("/tmp/test_sanitize_bench.dfy")
    for path in specs:
        cleaned = sanitize_dafny_skeleton(path.read_text())
        tmp.write_text(cleaned)
        result = resolve(tmp, allow_warnings=True)
        assert result.ok, f"{path.parent.name}: {result.stderr[:200]}"
