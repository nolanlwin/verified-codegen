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
  decreases |arr|
{
  if |arr| == 0 {
    result := [];
  } else {
    assert forall i :: 0 <= i < |arr[1..]| ==> arr[1..][i] >= 0 by {
      forall i | 0 <= i < |arr[1..]|
        ensures arr[1..][i] >= 0
      {
        assert arr[1..][i] == arr[i + 1];
        assert 0 <= i + 1 < |arr|;
      }
    }

    var tail := pluck(arr[1..]);

    if arr[0] % 2 == 0 {
      if |tail| < 2 {
        result := [arr[0], 0];
      } else if arr[0] <= tail[0] {
        result := [arr[0], 0];
      } else {
        result := [tail[0], tail[1] + 1];
      }
    } else {
      if |tail| < 2 {
        result := [];
      } else {
        result := [tail[0], tail[1] + 1];
      }
    }
  }
}
