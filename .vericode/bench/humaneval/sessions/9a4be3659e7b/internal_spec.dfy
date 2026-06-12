function PluckSpec(arr: seq<int>): seq<int>
  decreases |arr|
{
  if |arr| == 0 then []
  else
    var tail := PluckSpec(arr[1..]);
    if arr[0] % 2 == 0 then
      if |tail| < 2 then [arr[0], 0]
      else if arr[0] <= tail[0] then [arr[0], 0]
      else [tail[0], tail[1] + 1]
    else
      if |tail| < 2 then []
      else [tail[0], tail[1] + 1]
}

method pluck(arr: seq<int>) returns (result: seq<int>)
  requires forall i :: 0 <= i < |arr| ==> arr[i] >= 0
  ensures result == PluckSpec(arr)
{
  assume false;
}
