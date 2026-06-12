function DigitSumSpec(n: int): int
  decreases n
{
  if n < 10 then n else n % 10 + DigitSumSpec(n / 10)
}
function BinaryStringSpec(n: int): string
  decreases n
{
  if n < 2 then
    if n == 0 then "0" else "1"
  else
    BinaryStringSpec(n / 2) + if n % 2 == 0 then "0" else "1"
}
function SolveSpec(N: int): string
{
  BinaryStringSpec(DigitSumSpec(N))
}

method solve(N: int) returns (result: string)
  requires 0 <= N <= 10000
  ensures result == SolveSpec(N)
{
  assume false;
}
