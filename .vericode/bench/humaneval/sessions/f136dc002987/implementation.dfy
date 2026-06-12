function IncrListSpec(l: seq<int>): seq<int>
  decreases |l|
{
  if |l| == 0 then [] else [l[0] + 1] + IncrListSpec(l[1..])
}

method incr_list(l: seq<int>) returns (result: seq<int>)
  ensures result == IncrListSpec(l)
{
  if |l| == 0 {
    result := [];
  } else {
    var tail := incr_list(l[1..]);
    result := [l[0] + 1] + tail;
  }
}
