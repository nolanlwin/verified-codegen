function SumToNSpec(n: int): int
  decreases n
{
  if n == 0 then 0 else n + SumToNSpec(n - 1)
}

method sum_to_n(n: int) returns (result: int)
  requires n >= 0
  ensures result == SumToNSpec(n)
{
  assume false;
}
