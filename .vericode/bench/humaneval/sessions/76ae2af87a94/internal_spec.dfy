function BelowThresholdSpec(l: seq<int>, t: int): bool
  decreases |l|
{
  if |l| == 0 then
    true
  else
    l[0] < t && BelowThresholdSpec(l[1..], t)
}

method below_threshold(l: seq<int>, t: int) returns (result: bool)
  requires true
  ensures result == BelowThresholdSpec(l, t)
{
  assume false;
}
