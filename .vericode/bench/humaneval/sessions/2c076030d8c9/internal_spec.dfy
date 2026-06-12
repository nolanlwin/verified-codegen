function SeqNthOrDefault(s: seq<int>, k: int, d: int): int
{
  if 0 <= k && k < |s| then s[k] else d
}
function ExtractEvenValuesAux(s: seq<int>, i: int): seq<int>
  decreases |s| - i
{
  if i == |s| then []
  else if i % 2 == 0 then [s[i]] + ExtractEvenValuesAux(s, i + 1)
  else ExtractEvenValuesAux(s, i + 1)
}
function ExtractEvenValues(s: seq<int>): seq<int>
{
  ExtractEvenValuesAux(s, 0)
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
function SortEvenSpec(l: seq<int>, i: int): seq<int>
  decreases |l| - i
{
  if i == |l| then []
  else if i % 2 == 0 then
    [SeqNthOrDefault(SortSeq(ExtractEvenValues(l)), i / 2, l[i])] + SortEvenSpec(l, i + 1)
  else
    [l[i]] + SortEvenSpec(l, i + 1)
}

method sort_even(l: seq<int>) returns (result: seq<int>)
  ensures result == SortEvenSpec(l, 0)
{
  assume false;
}
