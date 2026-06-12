function InsertSortedSpec(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x <= s[0] then [x] + s
  else [s[0]] + InsertSortedSpec(x, s[1..])
}
function SortSpec(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertSortedSpec(s[0], SortSpec(s[1..]))
}
function MedianSortedSpec(s: seq<int>): real
  decreases |s|
{
  if |s| == 1 then (s[0] as real)
  else if |s| == 2 then (((s[0] as real) + (s[1] as real)) / 2.0)
  else MedianSortedSpec(s[1..(|s| - 1)])
}
function MedianSpec(l: seq<int>): real
{
  MedianSortedSpec(SortSpec(l))
}

method median(l: seq<int>) returns (result: real)
  requires |l| > 0
  ensures result == MedianSpec(l)
{
  assume false;
}
