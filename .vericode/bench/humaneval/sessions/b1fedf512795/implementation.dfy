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
  var s := DigitSum(N);
  result := BinaryString(s);
}

method DigitSum(n: int) returns (s: int)
  requires 0 <= n
  ensures s == DigitSumSpec(n)
  ensures 0 <= s
  decreases n
{
  if n < 10 {
    s := n;
  } else {
    var t := DigitSum(n / 10);
    assert 0 <= n % 10;
    s := n % 10 + t;
  }
}

method BinaryString(n: int) returns (r: string)
  requires 0 <= n
  ensures r == BinaryStringSpec(n)
  decreases n
{
  if n < 2 {
    if n == 0 {
      r := "0";
    } else {
      r := "1";
    }
  } else {
    var prefix := BinaryString(n / 2);
    if n % 2 == 0 {
      r := prefix + "0";
    } else {
      r := prefix + "1";
    }
  }
}
