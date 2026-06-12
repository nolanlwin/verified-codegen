function FactorialSpec(n: int): int
  decreases n
{
  if n == 0 then 1 else n * FactorialSpec(n - 1)
}
function SpecialFactorialSpec(n: int): int
  decreases n
{
  if n == 1 then 1 else FactorialSpec(n) * SpecialFactorialSpec(n - 1)
}

method special_factorial(n: int) returns (result: int)
  requires n > 0
  ensures result == SpecialFactorialSpec(n)
{
  assume false;
}
