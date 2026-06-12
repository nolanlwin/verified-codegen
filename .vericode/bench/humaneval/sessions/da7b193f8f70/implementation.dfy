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
  result := SolutionAuxMethod(lst, 0);
}

method SolutionAuxMethod(lst: seq<int>, i: int) returns (result: int)
  requires 0 <= i <= |lst|
  ensures result == SolutionAux(lst, i)
  decreases |lst| - i
{
  if i == |lst| {
    result := 0;
  } else {
    var tail := SolutionAuxMethod(lst, i + 1);
    if i % 2 == 0 && lst[i] % 2 != 0 {
      result := lst[i] + tail;
    } else {
      result := tail;
    }
  }
}
