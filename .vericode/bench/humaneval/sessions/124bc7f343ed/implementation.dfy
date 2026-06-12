function GreatestCommonDivisorSpec(a: int, b: int): int
  decreases if a < 0 then 2 else if b < 0 then 1 else 0, if b < 0 then -b else b
{
  if a < 0 then GreatestCommonDivisorSpec(-a, b)
  else if b < 0 then GreatestCommonDivisorSpec(a, -b)
  else if b == 0 then a
  else GreatestCommonDivisorSpec(b, a % b)
}

method greatest_common_divisor(a: int, b: int) returns (result: int)
  ensures result == GreatestCommonDivisorSpec(a, b)
  decreases if a < 0 then 2 else if b < 0 then 1 else 0, if b < 0 then -b else b
{
  if a < 0 {
    result := greatest_common_divisor(-a, b);
  } else if b < 0 {
    result := greatest_common_divisor(a, -b);
  } else if b == 0 {
    result := a;
  } else {
    result := greatest_common_divisor(b, a % b);
  }
}
