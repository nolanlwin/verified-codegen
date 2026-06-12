function FibSpec(n: int): int
  decreases n
{
  if n == 0 then 0 else if n == 1 then 1 else FibSpec(n - 1) + FibSpec(n - 2)
}

method fib(n: int) returns (result: int)
  requires n >= 0
  ensures result == FibSpec(n)
  decreases n
{
  if n == 0 {
    result := 0;
  } else if n == 1 {
    result := 1;
  } else {
    var a := fib(n - 1);
    var b := fib(n - 2);
    result := a + b;
  }
}
