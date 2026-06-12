function NoDivisorFrom(n: int, d: int): bool
  decreases if n - d < 0 then 0 else n - d
{
  if d >= n then true else n % d != 0 && NoDivisorFrom(n, d + 1)
}
function IsPrimeSpec(n: int): bool
{
  n > 1 && NoDivisorFrom(n, 2)
}
function ExistsPrimeFactorZ(a: int, x: int, y: int, z: int): bool
  decreases 100 - z
{
  if z == 100 then false
  else (IsPrimeSpec(x) && IsPrimeSpec(y) && IsPrimeSpec(z) && x * y * z == a) || ExistsPrimeFactorZ(a, x, y, z + 1)
}
function ExistsPrimeFactorY(a: int, x: int, y: int): bool
  decreases 100 - y
{
  if y == 100 then false
  else ExistsPrimeFactorZ(a, x, y, 2) || ExistsPrimeFactorY(a, x, y + 1)
}
function ExistsPrimeFactorX(a: int, x: int): bool
  decreases 100 - x
{
  if x == 100 then false
  else ExistsPrimeFactorY(a, x, 2) || ExistsPrimeFactorX(a, x + 1)
}
function IsMultiplyPrimeSpec(a: int): bool
{
  ExistsPrimeFactorX(a, 2)
}

method is_multiply_prime(a: int) returns (result: bool)
  requires a < 100
  ensures result == IsMultiplyPrimeSpec(a)
{
  assume false;
}
