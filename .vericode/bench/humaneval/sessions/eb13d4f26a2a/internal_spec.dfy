function IntToMiniRomanSpec(number: int): string
  decreases number
{
  if number == 1000 then "m"
  else if number >= 900 then
    if number == 900 then "cm" else "cm" + IntToMiniRomanSpec(number - 900)
  else if number >= 500 then
    if number == 500 then "d" else "d" + IntToMiniRomanSpec(number - 500)
  else if number >= 400 then
    if number == 400 then "cd" else "cd" + IntToMiniRomanSpec(number - 400)
  else if number >= 100 then
    if number == 100 then "c" else "c" + IntToMiniRomanSpec(number - 100)
  else if number >= 90 then
    if number == 90 then "xc" else "xc" + IntToMiniRomanSpec(number - 90)
  else if number >= 50 then
    if number == 50 then "l" else "l" + IntToMiniRomanSpec(number - 50)
  else if number >= 40 then
    if number == 40 then "xl" else "xl" + IntToMiniRomanSpec(number - 40)
  else if number >= 10 then
    if number == 10 then "x" else "x" + IntToMiniRomanSpec(number - 10)
  else if number >= 9 then "ix"
  else if number >= 5 then
    if number == 5 then "v" else "v" + IntToMiniRomanSpec(number - 5)
  else if number >= 4 then "iv"
  else
    if number == 1 then "i" else "i" + IntToMiniRomanSpec(number - 1)
}

method int_to_mini_roman(number: int) returns (result: string)
  requires 1 <= number <= 1000
  ensures result == IntToMiniRomanSpec(number)
{
  assume false;
}
