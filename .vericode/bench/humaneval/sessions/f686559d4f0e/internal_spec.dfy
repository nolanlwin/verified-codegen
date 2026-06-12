function DigitString(d: int): string
{
  if d == 0 then "0"
  else if d == 1 then "1"
  else if d == 2 then "2"
  else if d == 3 then "3"
  else if d == 4 then "4"
  else if d == 5 then "5"
  else if d == 6 then "6"
  else if d == 7 then "7"
  else if d == 8 then "8"
  else "9"
}
function IntToStringSpec(n: int): string
  decreases n
{
  if n < 10 then DigitString(n)
  else IntToStringSpec(n / 10) + DigitString(n % 10)
}
function ReverseStringSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else ReverseStringSpec(s[1..]) + [s[0]]
}
function CircularShiftSpec(digits: string, shift: int): string
  decreases shift
{
  ""
}
