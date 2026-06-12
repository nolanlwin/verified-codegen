datatype RoundedAvgResult = IntResult(i: int) | StringResult(s: string)
function RangeSumSpec(current: int, last: int): int
  decreases last - current + 1
{
  if current > last then 0
  else current + RangeSumSpec(current + 1, last)
}
function RoundHalfEvenSpec(numer: int, denom: int): int
{
  var q := numer / denom;
  var r := numer % denom;
  if 2 * r < denom then q
  else if 2 * r > denom then q + 1
  else if q % 2 == 0 then q
  else q + 1
}
function BinaryDigitSpec(bit: int): string
{
  if bit == 0 then "0" else "1"
}
function BinaryDigitsSpec(x: int): string
  decreases if x < 0 then 0 else x
{
  if x <= 0 then "0"
  else if x == 1 then "1"
  else BinaryDigitsSpec(x / 2) + BinaryDigitSpec(x % 2)
}
function RoundedAvgSpec(n: int, m: int): RoundedAvgResult
{
  if n > m then IntResult(-1)
  else
    var total := RangeSumSpec(n, m);
    var count := m - n + 1;
    StringResult("0b" + BinaryDigitsSpec(RoundHalfEvenSpec(total, count)))
}

method rounded_avg(n: int, m: int) returns (result: RoundedAvgResult)
  requires n > 0
  requires m > 0
  ensures result == RoundedAvgSpec(n, m)
{
  assume false;
}
