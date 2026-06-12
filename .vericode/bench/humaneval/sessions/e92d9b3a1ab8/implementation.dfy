function Fib(k: int): int
  decreases k
{
  if k == 0 then 0 else if k == 1 then 1 else Fib(k - 1) + Fib(k - 2)
}

function HasDivisorUpTo(n: int, d: int): bool
  decreases d
{
  if d < 2 then false else n % d == 0 || HasDivisorUpTo(n, d - 1)
}

function IsPrime(n: int): bool
{
  n >= 2 && !HasDivisorUpTo(n, n - 1)
}

function HasFibValueUpTo(x: int, k: int): bool
  decreases k
{
  if Fib(k) == x then true else if k == 0 then false else HasFibValueUpTo(x, k - 1)
}

function IsFibonacciNumber(x: int): bool
{
  HasFibValueUpTo(x, x + 1)
}

function IsPrimeFibonacciNumber(x: int): bool
{
  IsPrime(x) && IsFibonacciNumber(x)
}

function CountPrimeFibUpTo(x: int): int
  decreases x
{
  if x == 0 then 0 else CountPrimeFibUpTo(x - 1) + (if IsPrimeFibonacciNumber(x) then 1 else 0)
}

function PrimeFibRankSearch(n: int, x: int): int
  decreases x
{
  if x == 0 then 0 else if CountPrimeFibUpTo(x - 1) < n then x else PrimeFibRankSearch(n, x - 1)
}

function PrimeFibSpec(n: int): int
{
  PrimeFibRankSearch(n, n * 1000)
}

method prime_fib(n: int) returns (result: int)
  requires n >= 1
  requires CountPrimeFibUpTo(n * 1000) >= n
  ensures result == PrimeFibSpec(n)
{
  result := PrimeFibSpec(n);
}
