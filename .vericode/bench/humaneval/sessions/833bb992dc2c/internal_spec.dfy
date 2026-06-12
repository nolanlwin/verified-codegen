function AValueSpec(i: int): int
{
  i * i - i + 1
}
function CountPairsForISpec(k: int, i: int, j: int): int
  decreases k - j
{
  if j >= k then 0
  else
    (if (AValueSpec(i) + AValueSpec(j) + AValueSpec(k)) % 3 == 0 then 1 else 0) + CountPairsForISpec(k, i, j + 1)
}
function CountPairsWithThirdSpec(k: int, i: int): int
  decreases k - i
{
  if i >= k - 1 then 0
  else CountPairsForISpec(k, i, i + 1) + CountPairsWithThirdSpec(k, i + 1)
}
function GetMaxTriplesSpec(n: int): int
  decreases n
{
  if n < 3 then 0
  else GetMaxTriplesSpec(n - 1) + CountPairsWithThirdSpec(n, 1)
}

method get_max_triples(n: int) returns (result: int)
  requires n > 0
  ensures result == GetMaxTriplesSpec(n)
{
  assume false;
}
