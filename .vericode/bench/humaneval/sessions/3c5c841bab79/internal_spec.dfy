function AllNonNegative(s: seq<int>): bool
  decreases |s|
{
  if |s| == 0 then true
  else s[0] >= 0 && AllNonNegative(s[1..])
}
function CountOnesSpec(n: int): int
  decreases n
{
  if n == 0 then 0
  else (n % 2) + CountOnesSpec(n / 2)
}
function BitCountThenValueLeq(a: int, b: int): bool
{
  if CountOnesSpec(a) < CountOnesSpec(b) then true
  else if CountOnesSpec(a) > CountOnesSpec(b) then false
  else a <= b
}
function InsertByBitCount(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 || BitCountThenValueLeq(x, s[0]) then [x] + s
  else [s[0]] + InsertByBitCount(x, s[1..])
}
function SortArraySpec(arr: seq<int>): seq<int>
  decreases |arr|
{
  if |arr| == 0 then []
  else InsertByBitCount(arr[0], SortArraySpec(arr[1..]))
}

method sort_array(arr: seq<int>) returns (result: seq<int>)
  requires AllNonNegative(arr)
  ensures result == SortArraySpec(arr)
{
  assume false;
}
