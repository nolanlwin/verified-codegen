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
  if n <= 1 {
    result := false;
  } else {
    result := IsPrimeFrom(n, 2);
  }
}

method IsPrimeFrom(n: int, d: int) returns (result: bool)
  requires 2 <= d <= n
  ensures result == IsPrimeSpecFrom(n, d)
  decreases n - d
{
  if d == n {
    result := true;
  } else if n % d == 0 {
    result := false;
  } else {
    result := IsPrimeFrom(n, d + 1);
  }
}
