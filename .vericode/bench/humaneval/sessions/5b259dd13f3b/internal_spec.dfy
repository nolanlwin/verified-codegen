function InsertUniqueSorted(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then
    [x]
  else if x < s[0] then
    [x] + s
  else if x == s[0] then
    s
  else
    [s[0]] + InsertUniqueSorted(x, s[1..])
}
function UniqueSpec(l: seq<int>): seq<int>
  decreases |l|
{
  if |l| == 0 then
    []
  else
    InsertUniqueSorted(l[0], UniqueSpec(l[1..]))
}

method unique(l: seq<int>) returns (result: seq<int>)
  ensures result == UniqueSpec(l)
{
  assume false;
}
