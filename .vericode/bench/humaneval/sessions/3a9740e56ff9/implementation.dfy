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
  decreases n
{
  if n == 0 {
    result := 0;
  } else if n == 1 {
    result := 0;
  } else if n == 2 {
    result := 1;
  } else {
    assert n >= 3;
    var a := fibfib(n - 1);
    var b := fibfib(n - 2);
    var c := fibfib(n - 3);
    result := a + b + c;
  }
}
