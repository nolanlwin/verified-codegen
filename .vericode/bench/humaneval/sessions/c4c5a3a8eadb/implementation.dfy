function DigitString(d: int): string
{
  if d == 0 then "0" else
  if d == 1 then "1" else
  if d == 2 then "2" else
  if d == 3 then "3" else
  if d == 4 then "4" else
  if d == 5 then "5" else
  if d == 6 then "6" else
  if d == 7 then "7" else
  if d == 8 then "8" else "9"
}

function ChangeBaseSpec(x: int, base: int): string
  decreases x
{
  if x < base then DigitString(x) else ChangeBaseSpec(x / base, base) + DigitString(x % base)
}

method change_base(x: int, base: int) returns (result: string)
  requires x >= 0
  requires 2 <= base < 10
  ensures result == ChangeBaseSpec(x, base)
  decreases x
{
  if x < base {
    result := DigitString(x);
  } else {
    result := change_base(x / base, base);
    result := result + DigitString(x % base);
  }
}
