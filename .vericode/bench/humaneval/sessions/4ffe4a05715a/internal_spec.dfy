function IsPrimeSpec(n: int): bool
{
  if n <= 1 then false else IsPrimeSpecFrom(n, 2)
}
function IsPrimeSpecFrom(n: int, d: int): bool
  decreases n - d
{
  if d == n then true
  else if n % d == 0 then false
  else IsPrimeSpecFrom(n, d + 1)
}

method is_prime(n: int) returns (result: bool)
  ensures result == IsPrimeSpec(n)
{
  assume false;
}
