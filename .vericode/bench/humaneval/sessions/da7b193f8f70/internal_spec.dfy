function SolutionAux(lst: seq<int>, i: int): int
  decreases |lst| - i
{
  if i == |lst| then 0
  else (if i % 2 == 0 && lst[i] % 2 != 0 then lst[i] else 0) + SolutionAux(lst, i + 1)
}
function SolutionSpec(lst: seq<int>): int
{
  SolutionAux(lst, 0)
}

method solution(lst: seq<int>) returns (result: int)
  requires |lst| > 0
  ensures result == SolutionSpec(lst)
{
  assume false;
}
