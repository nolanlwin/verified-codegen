function DigitChar(d: int): char
{
  if d == 0 then '0'
  else if d == 1 then '1'
  else if d == 2 then '2'
  else if d == 3 then '3'
  else if d == 4 then '4'
  else if d == 5 then '5'
  else if d == 6 then '6'
  else if d == 7 then '7'
  else if d == 8 then '8'
  else '9'
}

function NatToStringSpec(n: int): string
  decreases n
{
  if n < 10 then [DigitChar(n)]
  else NatToStringSpec(n / 10) + [DigitChar(n % 10)]
}

function StringSequenceSpec(n: int): string
  decreases n
{
  if n == 0 then NatToStringSpec(0)
  else StringSequenceSpec(n - 1) + " " + NatToStringSpec(n)
}

method string_sequence(n: int) returns (result: string)
  requires n >= 0
  ensures result == StringSequenceSpec(n)
  decreases n
{
  if n == 0 {
    result := NatToStringSpec(0);
  } else {
    assert n > 0;
    assert n - 1 >= 0;
    var previous := string_sequence(n - 1);
    result := previous + " " + NatToStringSpec(n);
  }
}
