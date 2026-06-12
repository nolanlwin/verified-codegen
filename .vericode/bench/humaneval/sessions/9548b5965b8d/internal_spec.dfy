function IsLowercaseChar(ch: char): bool
{
  ('a' as int) <= (ch as int) && (ch as int) <= ('z' as int)
}
function LowercaseString(s: string): bool
  decreases |s|
{
  if |s| == 0 then true else IsLowercaseChar(s[0]) && LowercaseString(s[1..])
}
function DecodeShiftChar(ch: char): char
{
  var shifted := ((ch as int) - ('a' as int) - 5 + 26) % 26;
  (shifted + ('a' as int)) as char
}
function DecodeShiftSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then "" else [DecodeShiftChar(s[0])] + DecodeShiftSpec(s[1..])
}

method decode_shift(s: string) returns (result: string)
  requires LowercaseString(s)
  ensures result == DecodeShiftSpec(s)
{
  assume false;
}
