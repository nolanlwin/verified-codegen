function StripLastTwo(s: string): string
{
  if |s| <= 2 then "" else s[..|s| - 2]
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
  decreases decimal
{
  if decimal < 2 {
    if decimal == 0 {
      result := "db0db";
    } else {
      result := "db1db";
    }
  } else {
    assert decimal / 2 >= 0;
    assert decimal / 2 < decimal;
    var partial := decimal_to_binary(decimal / 2);
    result := StripLastTwo(partial) + BitChar(decimal) + "db";
  }
}
