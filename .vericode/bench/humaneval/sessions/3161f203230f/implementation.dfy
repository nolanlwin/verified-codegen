function ContainsValue(s: seq<int>, x: int): bool
  decreases |s|
{
  if |s| == 0 then false else s[0] == x || ContainsValue(s[1..], x)
}

function PairsSumToZeroSpec(l: seq<int>): bool
  decreases |l|
{
  if |l| < 2 then false else ContainsValue(l[1..], -l[0]) || PairsSumToZeroSpec(l[1..])
}

method pairs_sum_to_zero(l: seq<int>) returns (result: bool)
  ensures result == PairsSumToZeroSpec(l)
  decreases |l|
{
  if |l| < 2 {
    result := false;
  } else {
    if ContainsValue(l[1..], -l[0]) {
      result := true;
    } else {
      result := pairs_sum_to_zero(l[1..]);
    }
  }
}
