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
  var sorted := Sort(l);
  assert |sorted| > 0;
  result := MedianSorted(sorted);
  assert sorted == SortSpec(l);
  assert result == MedianSortedSpec(SortSpec(l));
}

method InsertSorted(x: int, s: seq<int>) returns (r: seq<int>)
  ensures r == InsertSortedSpec(x, s)
  ensures |r| == |s| + 1
  decreases |s|
{
  if |s| == 0 {
    r := [x];
  } else if x <= s[0] {
    r := [x] + s;
  } else {
    var tail := InsertSorted(x, s[1..]);
    r := [s[0]] + tail;
  }
}

method Sort(s: seq<int>) returns (r: seq<int>)
  ensures r == SortSpec(s)
  ensures |r| == |s|
  decreases |s|
{
  if |s| == 0 {
    r := [];
  } else {
    var sortedTail := Sort(s[1..]);
    r := InsertSorted(s[0], sortedTail);
  }
}

method MedianSorted(s: seq<int>) returns (result: real)
  requires |s| > 0
  ensures result == MedianSortedSpec(s)
  decreases |s|
{
  if |s| == 1 {
    result := s[0] as real;
  } else if |s| == 2 {
    result := ((s[0] as real) + (s[1] as real)) / 2.0;
  } else {
    assert |s| > 2;
    assert 0 <= 1 <= |s| - 1 <= |s|;
    assert |s[1..(|s| - 1)]| == |s| - 2;
    assert |s[1..(|s| - 1)]| > 0;
    result := MedianSorted(s[1..(|s| - 1)]);
  }
}
