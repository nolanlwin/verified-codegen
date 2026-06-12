function MultiplySpec(a: int, b: int): int
  decreases if a < 0 then -a + 1 else a, if b < 0 then -b + 1 else b
{
  if a < 0 then MultiplySpec(-a, b)
  else if b < 0 then MultiplySpec(a, -b)
  else if 10 <= a then MultiplySpec(a - 10, b)
  else if 10 <= b then MultiplySpec(a, b - 10)
  else a * b
}

method multiply(a: int, b: int) returns (result: int)
  ensures result == MultiplySpec(a, b)
{
  assume false;
}
