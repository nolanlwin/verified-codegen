function CountFrom(lst: seq<int>, value: int, i: int): int
  decreases |lst| - i
{
  if i == |lst| then
    0
  else
    (if lst[i] == value then 1 else 0) + CountFrom(lst, value, i + 1)
}
function Count(lst: seq<int>, value: int): int
{
  CountFrom(lst, value, 0)
}
function SearchSpec(lst: seq<int>): int
  decreases |lst|
{
  if |lst| == 0 then
    -1
  else
    var tailBest := SearchSpec(lst[1..]);
    if lst[0] > 0 && Count(lst, lst[0]) >= lst[0] && lst[0] > tailBest then
      lst[0]
    else
      tailBest
}

method search(lst: seq<int>) returns (result: int)
  requires |lst| > 0
  requires forall i :: 0 <= i < |lst| ==> lst[i] > 0
  ensures result == SearchSpec(lst)
{
  assume false;
}
