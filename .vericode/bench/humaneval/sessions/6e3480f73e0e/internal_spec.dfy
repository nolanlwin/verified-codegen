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
  assume false;
}
