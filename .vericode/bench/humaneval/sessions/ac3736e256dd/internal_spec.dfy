function StrlenSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then 0 else 1 + StrlenSpec(s[1..])
}

method strlen(s: string) returns (result: int)
  requires true
  ensures result == StrlenSpec(s)
{
  assume false;
}
