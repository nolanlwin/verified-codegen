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
  if n > m {
    result := IntResult(-1);
  } else {
    var total := RangeSum(n, m);
    var count := m - n + 1;
    assert count > 0;
    var rounded := RoundHalfEven(total, count);
    var digits := BinaryDigits(rounded);
    result := StringResult("0b" + digits);
  }
}

method RangeSum(current: int, last: int) returns (total: int)
  ensures total == RangeSumSpec(current, last)
  decreases last - current + 1
{
  if current > last {
    total := 0;
  } else {
    var rest := RangeSum(current + 1, last);
    total := current + rest;
  }
}

method RoundHalfEven(numer: int, denom: int) returns (rounded: int)
  requires denom > 0
  ensures rounded == RoundHalfEvenSpec(numer, denom)
{
  var q := numer / denom;
  var r := numer % denom;
  if 2 * r < denom {
    rounded := q;
  } else if 2 * r > denom {
    rounded := q + 1;
  } else if q % 2 == 0 {
    rounded := q;
  } else {
    rounded := q + 1;
  }
}

method BinaryDigit(bit: int) returns (s: string)
  ensures s == BinaryDigitSpec(bit)
{
  if bit == 0 {
    s := "0";
  } else {
    s := "1";
  }
}

method BinaryDigits(x: int) returns (s: string)
  ensures s == BinaryDigitsSpec(x)
  decreases if x < 0 then 0 else x
{
  if x <= 0 {
    s := "0";
  } else if x == 1 {
    s := "1";
  } else {
    assert x > 1;
    assert 0 <= x / 2;
    assert x / 2 < x;
    var prefix := BinaryDigits(x / 2);
    var digit := BinaryDigit(x % 2);
    s := prefix + digit;
  }
}
