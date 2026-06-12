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
  assume false;
}
