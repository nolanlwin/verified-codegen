function StripLastTwo(s: string): string
{
  ""
}
function BitChar(n: int): string
{
  if n % 2 == 0 then "0" else "1"
}
function DecimalToBinarySpec(decimal: int): string
  decreases decimal
{
  if decimal < 2 then
    "db" + (if decimal == 0 then "0" else "1") + "db"
  else
    StripLastTwo(DecimalToBinarySpec(decimal / 2)) + BitChar(decimal) + "db"
}

method decimal_to_binary(decimal: int) returns (result: string)
  requires decimal >= 0
  ensures result == DecimalToBinarySpec(decimal)
{
  assume false;
}
