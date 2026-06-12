function AddElementsSpec(arr: seq<int>, k: int): int
  decreases k
{
  if k <= 0 then
    0
  else if k > |arr| then
    AddElementsSpec(arr, |arr|)
  else if -99 <= arr[k - 1] <= 99 then
    AddElementsSpec(arr, k - 1) + arr[k - 1]
  else
    AddElementsSpec(arr, k - 1)
}

method AddElementsHelper(arr: seq<int>, k: int) returns (sum: int)
  requires 0 <= k <= |arr|
  ensures sum == AddElementsSpec(arr, k)
  decreases k
{
  if k == 0 {
    sum := 0;
  } else {
    var previous := AddElementsHelper(arr, k - 1);
    if -99 <= arr[k - 1] <= 99 {
      sum := previous + arr[k - 1];
    } else {
      sum := previous;
    }
  }
}

method AddElements(arr: seq<int>, k: int) returns (sum: int)
  requires 1 <= |arr| <= 100
  requires 1 <= k <= |arr|
  ensures sum == AddElementsSpec(arr, k)
{
  sum := AddElementsHelper(arr, k);
}
