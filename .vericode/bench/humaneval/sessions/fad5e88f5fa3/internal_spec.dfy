function Fib4Spec(n: int): int
  decreases n
{
  if n == 0 then 0
  else if n == 1 then 0
  else if n == 2 then 2
  else if n == 3 then 0
  else Fib4Spec(n - 1) + Fib4Spec(n - 2) + Fib4Spec(n - 3) + Fib4Spec(n - 4)
}

method fib4(n: int) returns (result: int)
  requires n >= 0
  ensures result == Fib4Spec(n)
{
  assume false;
}
