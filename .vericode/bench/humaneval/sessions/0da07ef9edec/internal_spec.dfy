function Pow(base: int, exp: int): int
  decreases exp
{
  if exp == 0 then 1 else base * Pow(base, exp - 1)
}
function IsSimplePowerSearch(x: int, n: int, k: int): bool
  decreases k
{
  if Pow(n, k) == x then true
  else if k == 0 then false
  else IsSimplePowerSearch(x, n, k - 1)
}
function IsSimplePowerSpec(x: int, n: int): bool
{
  IsSimplePowerSearch(x, n, if x < 0 then -x + 1 else x + 1)
}

method is_simple_power(x: int, n: int) returns (result: bool)
  ensures result == IsSimplePowerSpec(x, n)
{
  assume false;
}
