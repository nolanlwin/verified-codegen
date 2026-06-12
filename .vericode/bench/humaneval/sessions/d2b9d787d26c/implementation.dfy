function ModpSpec(n: int, p: int): int
  decreases n
{
  if n == 0 then 1 % p else (2 * ModpSpec(n - 1, p)) % p
}

method modp(n: int, p: int) returns (result: int)
  requires n >= 0
  requires p > 0
  ensures result == ModpSpec(n, p)
  decreases n
{
  if n == 0 {
    result := 1 % p;
  } else {
    assert n > 0;
    var r := modp(n - 1, p);
    result := (2 * r) % p;
    assert result == (2 * ModpSpec(n - 1, p)) % p;
    assert result == ModpSpec(n, p);
  }
}
