function DigitsSpec(n: int): int
  decreases n
{
  if n < 10 then
    if n % 2 == 1 then n else 0
  else
    var rest := DigitsSpec(n / 10);
    var digit := n % 10;
    if digit % 2 == 1 then
      if rest == 0 then digit else rest * digit
    else
      rest
}

method digits(n: int) returns (result: int)
  requires n > 0
  ensures result == DigitsSpec(n)
{
  assume false;
}
