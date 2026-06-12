function FactorizeSpec(n: int, d: int): seq<int>
  decreases n, n - d
{
  if n == 1 then []
  else if d * d > n then [n]
  else if n % d == 0 then [d] + FactorizeSpec(n / d, d)
  else FactorizeSpec(n, d + 1)
}

method factorize(n: int) returns (result: seq<int>)
  requires n > 1
  ensures result == FactorizeSpec(n, 2)
{
  result := FactorizeSpec(n, 2);
}
