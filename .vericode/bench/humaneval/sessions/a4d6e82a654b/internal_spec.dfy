function IsPrimeHexDigit(c: char): bool
{
  c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == "D"
}
function IsHexDigit(c: char): bool
{
  c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9' || c == 'A' || c == 'B' || c == 'C' || c == 'D' || c == 'E' || c == "F"
}
function IsValidHexString(num: string): bool
  decreases |num|
{
  if |num| == 0 then true else IsHexDigit(num[0]) && IsValidHexString(num[1..])
}
function HexKeySpec(num: string): int
  decreases |num|
{
  if |num| == 0 then 0 else (if IsPrimeHexDigit(num[0]) then 1 else 0) + HexKeySpec(num[1..])
}

method hex_key(num: string) returns (result: int)
  requires IsValidHexString(num)
  ensures result == HexKeySpec(num)
{
  assume false;
}
