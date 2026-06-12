function MoveOneBallDropCount(arr: seq<int>, i: int): int
  decreases |arr| - i
{
  if |arr| <= 1 || i >= |arr| then 0
  else
    var next := if i + 1 == |arr| then 0 else i + 1;
    (if arr[i] > arr[next] then 1 else 0) + MoveOneBallDropCount(arr, i + 1)
}
function MoveOneBallSpec(arr: seq<int>): bool
{
  if |arr| == 0 then true
  else MoveOneBallDropCount(arr, 0) <= 1
}

method move_one_ball(arr: seq<int>) returns (result: bool)
  ensures result == MoveOneBallSpec(arr)
{
  assume false;
}
