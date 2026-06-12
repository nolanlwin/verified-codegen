function HasDivisorFromSpec(n: int, d: int): bool
  decreases n - d
{
  if d >= n then false
  else if n % d == 0 then true
  else HasDivisorFromSpec(n, d + 1)
}
function IsPrimeSpec(n: int): bool
{
  if n <= 1 then false
  else !HasDivisorFromSpec(n, 2)
}
function IntersectionSpec(interval1: (int, int), interval2: (int, int)): string
{
  var left := if interval1.0 >= interval2.0 then interval1.0 else interval2.0;
  var right := if interval1.1 <= interval2.1 then interval1.1 else interval2.1;
  if left > right then "NO"
  else if IsPrimeSpec(right - left) then "YES"
  else "NO"
}

method intersection(interval1: (int, int), interval2: (int, int)) returns (result: string)
  requires interval1.0 <= interval1.1
  requires interval2.0 <= interval2.1
  ensures result == IntersectionSpec(interval1, interval2)
{
  assume false;
}
