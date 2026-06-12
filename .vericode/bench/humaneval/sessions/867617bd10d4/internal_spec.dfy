function CountDigitsNonNegSpec(n: int): (int, int)
  decreases n
{
  if n < 10 then
    if n % 2 == 0 then (1, 0) else (0, 1)
  else
    var rest := CountDigitsNonNegSpec(n / 10);
    if (n % 10) % 2 == 0 then (rest.0 + 1, rest.1) else (rest.0, rest.1 + 1)
}
function EvenOddCountSpec(num: int): (int, int)
{
  var n := if num < 0 then -num else num;
  CountDigitsNonNegSpec(n)
}

method even_odd_count(num: int) returns (result: (int, int))
  ensures result == EvenOddCountSpec(num)
{
  assume false;
}
