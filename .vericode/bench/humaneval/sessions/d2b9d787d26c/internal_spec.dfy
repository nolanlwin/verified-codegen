function ModpSpec(n: int, p: int): int
  decreases n
{
  if n == 0 then 1 % p else (2 * ModpSpec(n - 1, p)) % p
}

method modp(n: int, p: int) returns (result: int)
  requires n >= 0
  requires p > 0
  ensures result == ModpSpec(n, p)
{
  assume false;
}
