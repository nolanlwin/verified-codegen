function FactorialSpec(i: int): int
  requires i >= 0
  decreases i
{
  if i <= 1 then 1 else i * FactorialSpec(i - 1)
}

function SumToSpec(i: int): int
  requires i >= 0
  decreases i
{
  if i == 0 then 0 else i + SumToSpec(i - 1)
}

function ElementSpec(i: int): int
  requires i >= 0
{
  if i % 2 == 0 then FactorialSpec(i) else SumToSpec(i)
}

function FSpec(n: int): seq<int>
  requires n >= 0
  decreases n
{
  if n == 0 then [] else FSpec(n - 1) + [ElementSpec(n)]
}

method f(n: int) returns (result: seq<int>)
  requires n >= 0
  ensures result == FSpec(n)
  decreases n
{
  if n == 0 {
    result := [];
  } else {
    var prev := f(n - 1);
    result := prev + [ElementSpec(n)];
  }
}
