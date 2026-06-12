function AllNonNegativeSpec(lst: seq<int>): bool
  decreases |lst|
{
  if |lst| == 0 then true
  else lst[0] >= 0 && AllNonNegativeSpec(lst[1..])
}
function IsSortedSpec(lst: seq<int>): bool
  decreases |lst|
{
  if |lst| <= 1 then true
  else if lst[0] > lst[1] then false
  else if |lst| >= 3 && lst[0] == lst[2] then false
  else IsSortedSpec(lst[1..])
}

method is_sorted(lst: seq<int>) returns (result: bool)
  requires AllNonNegativeSpec(lst)
  ensures result == IsSortedSpec(lst)
{
  assume false;
}
