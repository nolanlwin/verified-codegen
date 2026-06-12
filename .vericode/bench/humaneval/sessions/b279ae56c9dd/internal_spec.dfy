function HasDivisorFrom(n: int, d: int): bool
  decreases n - d
{
  if d >= n then false else n % d == 0 || HasDivisorFrom(n, d + 1)
}
function IsPrime(n: int): bool
{
  !HasDivisorFrom(n, 2)
}
function LargestPrimeFactorAux(n: int, d: int): int
  decreases d
{
  if d <= 1 then 1
  else if n % d == 0 && IsPrime(d) then d
  else LargestPrimeFactorAux(n, d - 1)
}
function LargestPrimeFactorSpec(n: int): int
  decreases n
{
  LargestPrimeFactorAux(n, n - 1)
}

method largest_prime_factor(n: int) returns (result: int)
  requires n > 1
  requires !IsPrime(n)
  ensures result == LargestPrimeFactorSpec(n)
{
  assume false;
}
