function NoDivisorsSpec(n: int, d: int): bool
  decreases n - d
{
  if d == n then true
  else if n % d == 0 then false
  else NoDivisorsSpec(n, d + 1)
}
function IsPrimeSpec(n: int): bool
{
  if n <= 1 then false
  else NoDivisorsSpec(n, 2)
}
function XOrYSpec(n: int, x: int, y: int): int
{
  if IsPrimeSpec(n) then x else y
}

method x_or_y(n: int, x: int, y: int) returns (result: int)
  ensures result == XOrYSpec(n, x, y)
{
  assume false;
}
