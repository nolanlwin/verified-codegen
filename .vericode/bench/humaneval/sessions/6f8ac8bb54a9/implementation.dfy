function MaxElementSpec(l: seq<int>): int
  decreases |l|
{
  if |l| == 1 then
    l[0]
  else
    var tailMax := MaxElementSpec(l[1..]);
    if l[0] >= tailMax then l[0] else tailMax
}

method max_element(l: seq<int>) returns (result: int)
  requires |l| > 0
  ensures result == MaxElementSpec(l)
  decreases |l|
{
  if |l| == 1 {
    result := l[0];
  } else {
    assert |l| > 1;
    var tailMax := max_element(l[1..]);
    if l[0] >= tailMax {
      result := l[0];
    } else {
      result := tailMax;
    }
  }
}
