function CanArrangeSpec(arr: seq<int>): int
  decreases |arr|
{
  if |arr| <= 1 then
    -1
  else if arr[|arr| - 1] < arr[|arr| - 2] then
    |arr| - 1
  else
    CanArrangeSpec(arr[..|arr| - 1])
}

method CanArrange(arr: seq<int>) returns (r: int)
  ensures r == CanArrangeSpec(arr)
  decreases |arr|
{
  if |arr| <= 1 {
    r := -1;
  } else if arr[|arr| - 1] < arr[|arr| - 2] {
    r := |arr| - 1;
  } else {
    r := CanArrange(arr[..|arr| - 1]);
  }
}
