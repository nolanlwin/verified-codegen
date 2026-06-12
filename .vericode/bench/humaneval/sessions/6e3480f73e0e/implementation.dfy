datatype IntOption = None | Some(value: int)

function MinSeq(s: seq<int>): int
  decreases |s|
{
  if |s| == 1 then s[0] else
    var tailMin := MinSeq(s[1..]);
    if s[0] <= tailMin then s[0] else tailMin
}

function MinGreaterThan(s: seq<int>, threshold: int): IntOption
  decreases |s|
{
  if |s| == 0 then None else
    var tailBest := MinGreaterThan(s[1..], threshold);
    if s[0] <= threshold then tailBest else
      match tailBest
      case None => Some(s[0])
      case Some(v) => if s[0] <= v then Some(s[0]) else Some(v)
}

function NextSmallestSpec(lst: seq<int>): IntOption
  decreases |lst|
{
  if |lst| == 0 then None else
    var smallest := MinSeq(lst);
    MinGreaterThan(lst, smallest)
}

method next_smallest(lst: seq<int>) returns (result: IntOption)
  requires true
  ensures result == NextSmallestSpec(lst)
{
  if |lst| == 0 {
    result := None;
  } else {
    var smallest := MinSeqImpl(lst);
    result := MinGreaterThanImpl(lst, smallest);
  }
}

method MinSeqImpl(s: seq<int>) returns (m: int)
  requires |s| > 0
  ensures m == MinSeq(s)
  decreases |s|
{
  if |s| == 1 {
    m := s[0];
  } else {
    assert |s| > 1;
    var tail := s[1..];
    assert |tail| == |s| - 1;
    assert |tail| > 0;
    var tailMin := MinSeqImpl(tail);
    if s[0] <= tailMin {
      m := s[0];
    } else {
      m := tailMin;
    }
  }
}

method MinGreaterThanImpl(s: seq<int>, threshold: int) returns (r: IntOption)
  ensures r == MinGreaterThan(s, threshold)
  decreases |s|
{
  if |s| == 0 {
    r := None;
  } else {
    var tail := s[1..];
    assert |tail| == |s| - 1;
    var tailBest := MinGreaterThanImpl(tail, threshold);
    if s[0] <= threshold {
      r := tailBest;
    } else {
      r := match tailBest
           case None => Some(s[0])
           case Some(v) => if s[0] <= v then Some(s[0]) else Some(v);
    }
  }
}
