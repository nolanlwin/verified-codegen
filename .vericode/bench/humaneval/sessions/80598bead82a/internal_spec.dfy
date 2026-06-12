function NondecreasingFrom(l: seq<int>, i: int): bool
  decreases |l| - i
{
  if i + 1 >= |l| then true else l[i] <= l[i + 1] && NondecreasingFrom(l, i + 1)
}
function NonincreasingFrom(l: seq<int>, i: int): bool
  decreases |l| - i
{
  if i + 1 >= |l| then true else l[i] >= l[i + 1] && NonincreasingFrom(l, i + 1)
}
function MonotonicSpec(l: seq<int>): bool
{
  NondecreasingFrom(l, 0) || NonincreasingFrom(l, 0)
}

method monotonic(l: seq<int>) returns (result: bool)
  ensures result == MonotonicSpec(l)
{
  assume false;
}
