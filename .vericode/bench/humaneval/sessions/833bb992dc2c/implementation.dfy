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
  decreases n
{
  if n < 3 {
    result := 0;
  } else {
    var previous := get_max_triples(n - 1);
    var added := CountPairsWithThird(n, 1);
    result := previous + added;
  }
}

method CountPairsForI(k: int, i: int, j: int) returns (result: int)
  ensures result == CountPairsForISpec(k, i, j)
  decreases k - j
{
  if j >= k {
    result := 0;
  } else {
    var rest := CountPairsForI(k, i, j + 1);
    if (AValueSpec(i) + AValueSpec(j) + AValueSpec(k)) % 3 == 0 {
      result := 1 + rest;
    } else {
      result := rest;
    }
  }
}

method CountPairsWithThird(k: int, i: int) returns (result: int)
  ensures result == CountPairsWithThirdSpec(k, i)
  decreases k - i
{
  if i >= k - 1 {
    result := 0;
  } else {
    var first := CountPairsForI(k, i, i + 1);
    var rest := CountPairsWithThird(k, i + 1);
    result := first + rest;
  }
}
