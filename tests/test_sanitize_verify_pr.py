from vericode.dafny.sanitize import sanitize_dafny_implementation

MAKE_A_PILE_IMPL = """
function MakeAPileAux(start: int, count: int): seq<int>
  requires count >= 0
  decreases count
{ if count == 0 then [] else [start] + MakeAPileAux(start + 2, count - 1) }

method MakeAPile(start: int, count: int) returns (result: seq<int>)
  requires count >= 0
  ensures result == MakeAPileAux(start, count)
{
  result := [];
}
"""


def test_skip_benchmark_injection_preserves_stub_body() -> None:
    out = sanitize_dafny_implementation(MAKE_A_PILE_IMPL, skip_benchmark_injection=True)
    assert "result := [];" in out
    assert "result := [start] + tail" not in out


def test_greenfield_injection_replaces_make_a_pile() -> None:
    out = sanitize_dafny_implementation(MAKE_A_PILE_IMPL, skip_benchmark_injection=False)
    assert "result := [start] + tail" in out
