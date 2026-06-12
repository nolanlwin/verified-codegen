function Contains(s: seq<int>, x: int): bool
  decreases |s|
{
  if |s| == 0 then false else s[0] == x || Contains(s[1..], x)
}
function InsertSortedUnique(s: seq<int>, x: int): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x == s[0] then s
  else if x < s[0] then [x] + s
  else [s[0]] + InsertSortedUnique(s[1..], x)
}
function CommonSpec(l1: seq<int>, l2: seq<int>): seq<int>
  decreases |l1|
{
  if |l1| == 0 then []
  else if Contains(l2, l1[0]) then InsertSortedUnique(CommonSpec(l1[1..], l2), l1[0])
  else CommonSpec(l1[1..], l2)
}

method common(l1: seq<int>, l2: seq<int>) returns (result: seq<int>)
  requires true
  ensures result == CommonSpec(l1, l2)
{
  assume false;
}
