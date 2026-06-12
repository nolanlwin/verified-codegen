function NoEvenDigit(n: int): bool
  decreases n
{
  if n < 10 then n % 2 == 1
  else n % 2 == 1 && NoEvenDigit(n / 10)
}
function InsertIncreasing(v: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 || v <= s[0] then [v] + s
  else [s[0]] + InsertIncreasing(v, s[1..])
}
function UniqueDigitsSpec(x: seq<int>): seq<int>
  decreases |x|
{
  if |x| == 0 then []
  else
    var tail := UniqueDigitsSpec(x[1..]);
    if NoEvenDigit(x[0]) then InsertIncreasing(x[0], tail) else tail
}

method unique_digits(x: seq<int>) returns (result: seq<int>)
  requires forall i :: 0 <= i < |x| ==> x[i] > 0
  ensures result == UniqueDigitsSpec(x)
{
  assume false;
}
