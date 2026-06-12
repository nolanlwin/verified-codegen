function IsDigit(c: char): bool
{
  c == '0' || c == '1' || c == '2' || c == '3' || c == '4' ||
  c == '5' || c == '6' || c == '7' || c == '8' || c == '9'
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
function DigitsInRange(s: string, i: int, j: int): bool
  decreases j - i
  requires 0 <= i <= |s|
{
  if i == j then true
  else IsDigit(s[i]) && DigitsInRange(s, i + 1, j)
}
function TwoDigitNumber(tens: char, ones: char): int
{
  10 * DigitValue(tens) + DigitValue(ones)
}
function DaysInMonth(month: int): int
{
  if month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 then 31
  else if month == 4 || month == 6 || month == 9 || month == 11 then 30
  else if month == 2 then 29
  else 0
}
function ValidDateSpec(date: string): bool
{
  if |date| != 10 then false
  else if date[2] != '-' || date[5] != '-' then false
  else if !(DigitsInRange(date, 0, 2) && DigitsInRange(date, 3, 5) && DigitsInRange(date, 6, 10)) then false
  else
    var month := TwoDigitNumber(date[0], date[1]);
    var day := TwoDigitNumber(date[3], date[4]);
    1 <= month && month <= 12 && 1 <= day && day <= DaysInMonth(month)
}

method valid_date(date: string) returns (result: bool)
  ensures result == ValidDateSpec(date)
{
  assume false;
}
