function TransformAtIndex(x: int, i: int): int
{
  if i % 3 == 0 then x * x
  else if i % 4 == 0 then x * x * x
  else x
}

function SumSquaresAux(lst: seq<int>, i: int): int
  decreases |lst| - i
{
  if i == |lst| then 0
  else TransformAtIndex(lst[i], i) + SumSquaresAux(lst, i + 1)
}

function SumSquaresSpec(lst: seq<int>): int
{
  SumSquaresAux(lst, 0)
}

method sum_squares(lst: seq<int>) returns (result: int)
  ensures result == SumSquaresSpec(lst)
{
  result := SumSquaresAuxImpl(lst, 0);
  assert SumSquaresSpec(lst) == SumSquaresAux(lst, 0);
}

method SumSquaresAuxImpl(lst: seq<int>, i: int) returns (r: int)
  requires 0 <= i <= |lst|
  ensures r == SumSquaresAux(lst, i)
  decreases |lst| - i
{
  if i == |lst| {
    r := 0;
    assert SumSquaresAux(lst, i) == 0;
  } else {
    assert 0 <= i < |lst|;

    var transformed: int;
    if i % 3 == 0 {
      transformed := lst[i] * lst[i];
    } else if i % 4 == 0 {
      transformed := lst[i] * lst[i] * lst[i];
    } else {
      transformed := lst[i];
    }

    var rest: int;
    rest := SumSquaresAuxImpl(lst, i + 1);
    r := transformed + rest;

    assert transformed == TransformAtIndex(lst[i], i);
    assert rest == SumSquaresAux(lst, i + 1);
    assert SumSquaresAux(lst, i) == TransformAtIndex(lst[i], i) + SumSquaresAux(lst, i + 1);
  }
}
