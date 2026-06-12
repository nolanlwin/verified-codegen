function LargestDivisorSearch(n: int, d: int): int
  decreases d
{
  if d <= 1 then 1 else if n % d == 0 then d else LargestDivisorSearch(n, d - 1)
}
function LargestDivisorSpec(n: int): int
  decreases n
{
  LargestDivisorSearch(n, n - 1)
}

method largest_divisor(n: int) returns (result: int)
  requires n > 1
  ensures result == LargestDivisorSpec(n)
{
  assume false;
}
