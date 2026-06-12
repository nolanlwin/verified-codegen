function SmallestChangeSpec(arr: seq<int>): int
  decreases |arr|
{
  if |arr| <= 1 then
    0
  else
    (if arr[0] == arr[|arr| - 1] then 0 else 1) + SmallestChangeSpec(arr[1..|arr| - 1])
}

method smallest_change(arr: seq<int>) returns (result: int)
  ensures result == SmallestChangeSpec(arr)
  decreases |arr|
{
  if |arr| <= 1 {
    result := 0;
  } else {
    var inner := smallest_change(arr[1..|arr| - 1]);
    if arr[0] == arr[|arr| - 1] {
      result := inner;
    } else {
      result := inner + 1;
    }
  }
}
