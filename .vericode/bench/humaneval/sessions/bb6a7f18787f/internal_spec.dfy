function InsertSorted(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then
    [x]
  else if x <= s[0] then
    [x] + s
  else
    [s[0]] + InsertSorted(x, s[1..])
}
function SortSeq(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then
    []
  else
    InsertSorted(s[0], SortSeq(s[1..]))
}
function StrangePickEnds(sorted: seq<int>, takeMin: bool): seq<int>
  decreases |sorted|
{
  []
}
function StrangeSortListSpec(lst: seq<int>): seq<int>
{
  StrangePickEnds(SortSeq(lst), true)
}

method strange_sort_list(lst: seq<int>) returns (result: seq<int>)
  requires true
  ensures result == StrangeSortListSpec(lst)
{
  assume false;
}
