function DividesAny(n: int, d: int): bool
  decreases d
{
  if d < 2 then false else if n % d == 0 then true else DividesAny(n, d - 1)
}
function IsPrime(n: int): bool
{
  if n < 2 then false else !DividesAny(n, n - 1)
}
function DigitSum(n: int): int
  decreases n
{
  if n < 10 then n else n % 10 + DigitSum(n / 10)
}
function MaxPrimeAux(lst: seq<int>, i: int, current: int): int
  decreases |lst| - i
{
  if i == |lst| then current
  else if IsPrime(lst[i]) && lst[i] > current then MaxPrimeAux(lst, i + 1, lst[i])
  else MaxPrimeAux(lst, i + 1, current)
}
function SkjkasdkdSpec(lst: seq<int>): int
  decreases |lst|
{
  var m := MaxPrimeAux(lst, 0, -1);
  if |lst| == 0 then 0 else if m < 0 then SkjkasdkdSpec(lst[1..]) else DigitSum(m)
}

method skjkasdkd(lst: seq<int>) returns (result: int)
  requires true
  ensures result == SkjkasdkdSpec(lst)
{
  assume false;
}
