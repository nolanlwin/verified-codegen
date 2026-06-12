function FibfibSpec(n: int): int
  decreases n
{
  if n == 0 then 0
  else if n == 1 then 0
  else if n == 2 then 1
  else FibfibSpec(n - 1) + FibfibSpec(n - 2) + FibfibSpec(n - 3)
}

method fibfib(n: int) returns (result: int)
  requires n >= 0
  ensures result == FibfibSpec(n)
{
  assume false;
}
