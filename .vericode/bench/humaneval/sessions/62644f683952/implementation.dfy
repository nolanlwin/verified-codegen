function TriValueSpec(k: int): int
  decreases k
{
  if k == 0 then 1
  else if k == 1 then 3
  else if k % 2 == 0 then 1 + k / 2
  else (1 + (k - 1) / 2) + TriValueSpec(k - 2) + (1 + (k + 1) / 2)
}

function TriSpec(n: int): seq<int>
  decreases n
{
  if n == 0 then [TriValueSpec(0)]
  else TriSpec(n - 1) + [TriValueSpec(n)]
}

method tri(n: int) returns (result: seq<int>)
  requires n >= 0
  ensures result == TriSpec(n)
  decreases n
{
  if n == 0 {
    result := [TriValueSpec(0)];
  } else {
    var previous := tri(n - 1);
    result := previous + [TriValueSpec(n)];
  }
}
