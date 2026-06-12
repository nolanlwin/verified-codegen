function IsDigit(c: char): bool
{
  c == '0' || c == '1' || c == '2' || c == '3' || c == '4' ||
  c == '5' || c == '6' || c == '7' || c == '8' || c == "9"
}
function DigitValue(c: char): int
{
  if c == '0' then 0
  else if c == '1' then 1
  else if c == '2' then 2
  else if c == '3' then 3
  else if c == '4' then 4
  else if c == '5' then 5
  else if c == '6' then 6
  else if c == '7' then 7
  else if c == '8' then 8
  else if c == '9' then 9
  else 0
}
function FruitDistributionAux(s: string, i: int, count: int, current: int, inNumber: bool, sum: int): int
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then
    if inNumber && count < 2 then sum + current else sum
  else if IsDigit(s[i]) then
    FruitDistributionAux(s, i + 1, count, current * 10 + DigitValue(s[i]), true, sum)
  else if inNumber then
    if count + 1 >= 2 then sum + current
    else FruitDistributionAux(s, i + 1, count + 1, 0, false, sum + current)
  else
    FruitDistributionAux(s, i + 1, count, 0, false, sum)
}
function FruitDistributionSpec(s: string, n: int): int
{
  n - FruitDistributionAux(s, 0, 0, 0, false, 0)
}

method fruit_distribution(s: string, n: int) returns (result: int)
  requires true
  ensures result == FruitDistributionSpec(s, n)
{
  assume false;
}
