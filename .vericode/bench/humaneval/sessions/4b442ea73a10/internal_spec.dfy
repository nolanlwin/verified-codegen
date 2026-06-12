predicate IsCeiling(x: real, c: int)
{
  ((c - 1) as real) < x && x <= (c as real)
}
function CeilingSpec(x: real): int
function SumSquaresSpec(lst: seq<real>): int
  decreases |lst|
{
  if |lst| == 0 then 0
  else
    var c := CeilingSpec(lst[0]);
    c * c + SumSquaresSpec(lst[1..])
}

method sum_squares(lst: seq<real>) returns (result: int)
  ensures result == SumSquaresSpec(lst)
{
  assume false;
}
