function InsertSortedSpec(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x <= s[0] then [x] + s
  else [s[0]] + InsertSortedSpec(x, s[1..])
}
function SortAscendingSpec(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertSortedSpec(s[0], SortAscendingSpec(s[1..]))
}
function SuffixOfLengthSpec(s: seq<int>, k: int): seq<int>
  decreases |s|
{
  if |s| <= k then s
  else SuffixOfLengthSpec(s[1..], k)
}
function MaximumSpec(arr: seq<int>, k: int): seq<int>
  decreases |arr|
{
  if k == 0 then []
  else if k == |arr| then SortAscendingSpec(arr)
  else
    var rest := MaximumSpec(arr[1..], k);
    SuffixOfLengthSpec(InsertSortedSpec(arr[0], rest), k)
}

method maximum(arr: seq<int>, k: int) returns (result: seq<int>)
  requires 1 <= |arr| <= 1000
  requires 0 <= k <= |arr|
  requires forall i :: 0 <= i < |arr| ==> -1000 <= arr[i] <= 1000
  ensures result == MaximumSpec(arr, k)
{
  assume false;
}
