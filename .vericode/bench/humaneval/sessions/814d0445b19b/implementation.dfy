function TakeThirdValues(l: seq<int>, i: int): seq<int>
  decreases |l| - i
{
  if i == |l| then []
  else if i % 3 == 0 then [l[i]] + TakeThirdValues(l, i + 1)
  else TakeThirdValues(l, i + 1)
}

function InsertSorted(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x <= s[0] then [x] + s
  else [s[0]] + InsertSorted(x, s[1..])
}

function SortSeq(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertSorted(s[0], SortSeq(s[1..]))
}

function SortThirdSpec(l: seq<int>, sortedThirdValues: seq<int>, i: int, k: int): seq<int>
  decreases |l| - i
{
  if i == |l| then []
  else if i % 3 == 0 then
    if k < |sortedThirdValues| then [sortedThirdValues[k]] + SortThirdSpec(l, sortedThirdValues, i + 1, k + 1)
    else [l[i]] + SortThirdSpec(l, sortedThirdValues, i + 1, k)
  else [l[i]] + SortThirdSpec(l, sortedThirdValues, i + 1, k)
}

method sort_third(l: seq<int>) returns (result: seq<int>)
  requires true
  ensures result == SortThirdSpec(l, SortSeq(TakeThirdValues(l, 0)), 0, 0)
{
  result := SortThirdSpec(l, SortSeq(TakeThirdValues(l, 0)), 0, 0);
}
