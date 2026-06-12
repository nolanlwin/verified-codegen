function IsDigitChar(c: char): bool
{
  '0' <= c && c <= '9'
}

function IsOddDigitChar(c: char): bool
{
  c == '1' || c == '3' || c == '5' || c == '7' || c == '9'
}

function IsDigitString(s: string): bool
  decreases |s|
{
  if |s| == 0 then true
  else IsDigitChar(s[0]) && IsDigitString(s[1..])
}

function AllDigitStrings(lst: seq<string>): bool
  decreases |lst|
{
  if |lst| == 0 then true
  else IsDigitString(lst[0]) && AllDigitStrings(lst[1..])
}

function CountOddDigitsSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else (if IsOddDigitChar(s[0]) then 1 else 0) + CountOddDigitsSpec(s[1..])
}

function DigitToString(n: int): string
{
  if n == 0 then "0"
  else if n == 1 then "1"
  else if n == 2 then "2"
  else if n == 3 then "3"
  else if n == 4 then "4"
  else if n == 5 then "5"
  else if n == 6 then "6"
  else if n == 7 then "7"
  else if n == 8 then "8"
  else "9"
}

function IntToString(n: int): string
  decreases if n < 0 then 1 else 0, if n < 0 then -n else n
{
  if n < 0 then "-" + IntToString(-n)
  else if n < 10 then DigitToString(n)
  else IntToString(n / 10) + DigitToString(n % 10)
}

function OddCountMessage(count: int): string
{
  var t := IntToString(count);
  "the number of odd elements " + t + "n the str" + t + "ng " + t + " of the " + t + "nput."
}

function OddCountSpec(lst: seq<string>): seq<string>
  decreases |lst|
{
  if |lst| == 0 then []
  else [OddCountMessage(CountOddDigitsSpec(lst[0]))] + OddCountSpec(lst[1..])
}

method odd_count(lst: seq<string>) returns (result: seq<string>)
  requires AllDigitStrings(lst)
  ensures result == OddCountSpec(lst)
  decreases |lst|
{
  if |lst| == 0 {
    result := [];
  } else {
    assert AllDigitStrings(lst[1..]);
    var tail := odd_count(lst[1..]);
    result := [OddCountMessage(CountOddDigitsSpec(lst[0]))] + tail;
  }
}
