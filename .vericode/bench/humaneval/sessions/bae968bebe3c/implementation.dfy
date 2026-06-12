function HasProperDivisor(n: int, d: int): bool
  decreases d
{
  if d < 2 then false
  else if n % d == 0 then true
  else HasProperDivisor(n, d - 1)
}

function IsPrime(n: int): bool
{
  if n < 2 then false
  else !HasProperDivisor(n, n - 1)
}

function PrimeLengthSpec(s: string): bool
{
  IsPrime(|s|)
}

method prime_length(s: string) returns (result: bool)
  ensures result == PrimeLengthSpec(s)
{
  result := PrimeLengthSpec(s);
}
