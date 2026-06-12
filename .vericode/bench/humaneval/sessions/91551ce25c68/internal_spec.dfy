function IsDigit(c: char): bool
{
  c == '0' || c == '1' || c == '2' || c == '3' || c == '4' ||
  c == '5' || c == '6' || c == '7' || c == '8' || c == "9"
}
function DigitVal(c: char): int
{
  if c == '0' then 0 else
  if c == '1' then 1 else
  if c == '2' then 2 else
  if c == '3' then 3 else
  if c == '4' then 4 else
  if c == '5' then 5 else
  if c == '6' then 6 else
  if c == '7' then 7 else
  if c == '8' then 8 else
  if c == '9' then 9 else 0
}
function ValidNumberAux(s: string, i: int, seenDot: bool, digitsBefore: bool, digitsAfter: bool): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then
    digitsBefore && (if seenDot then digitsAfter else true)
  else if s[i] == '.' then
    !seenDot && ValidNumberAux(s, i + 1, true, digitsBefore, digitsAfter)
  else if IsDigit(s[i]) then
    if seenDot then
      ValidNumberAux(s, i + 1, seenDot, digitsBefore, true)
    else
      ValidNumberAux(s, i + 1, seenDot, true, digitsAfter)
  else
    false
}
function IsValidNumberString(s: string): bool
{
  if |s| == 0 then
    false
  else if s[0] == '-' then
    if |s| == 1 then false else ValidNumberAux(s, 1, false, false, false)
  else
    ValidNumberAux(s, 0, false, false, false)
}
function ClosestIntegerAux(s: string, i: int, sign: int, seenDot: bool, intPart: int, fracPart: int, scale: int): int
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then
    var roundedMag := if 2 * fracPart >= scale then intPart + 1 else intPart;
    sign * roundedMag
  else if s[i] == '.' then
    ClosestIntegerAux(s, i + 1, sign, true, intPart, fracPart, scale)
  else if seenDot then
    ClosestIntegerAux(s, i + 1, sign, true, intPart, fracPart * 10 + DigitVal(s[i]), scale * 10)
  else
    ClosestIntegerAux(s, i + 1, sign, false, intPart * 10 + DigitVal(s[i]), fracPart, scale)
}
function ClosestIntegerSpec(value: string): int
{
  if value[0] == '-' then
    ClosestIntegerAux(value, 1, -1, false, 0, 0, 1)
  else
    ClosestIntegerAux(value, 0, 1, false, 0, 0, 1)
}

method closest_integer(value: string) returns (result: int)
  requires |value| > 0
  requires IsValidNumberString(value)
  ensures result == ClosestIntegerSpec(value)
{
  assume false;
}
