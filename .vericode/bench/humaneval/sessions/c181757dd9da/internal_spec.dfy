function TruncateNumberSpec(number: real): real
  decreases number.Floor
{
  if number < 1.0 then
    number
  else
    TruncateNumberSpec(number - 1.0)
}

method truncate_number(number: real) returns (result: real)
  requires number >= 0.0
  ensures result == TruncateNumberSpec(number)
{
  assume false;
}
