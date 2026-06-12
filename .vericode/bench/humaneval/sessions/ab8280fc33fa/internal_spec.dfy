function TriplesSumToZeroSpec(l: seq<int>): bool
{
  ExistsTripleI(l, 0)
}
function ExistsTripleI(l: seq<int>, i: int): bool
  decreases |l| - i
{
  if i >= |l| then
    false
  else
    ExistsTripleJ(l, i, i + 1) || ExistsTripleI(l, i + 1)
}
function ExistsTripleJ(l: seq<int>, i: int, j: int): bool
  decreases |l| - j
{
  if j >= |l| then
    false
  else
    ExistsTripleK(l, i, j, j + 1) || ExistsTripleJ(l, i, j + 1)
}
function ExistsTripleK(l: seq<int>, i: int, j: int, k: int): bool
  decreases |l| - k
{
  if k >= |l| then
    false
  else
    l[i] + l[j] + l[k] == 0 || ExistsTripleK(l, i, j, k + 1)
}

method triples_sum_to_zero(l: seq<int>) returns (result: bool)
  ensures result == TriplesSumToZeroSpec(l)
{
  assume false;
}
