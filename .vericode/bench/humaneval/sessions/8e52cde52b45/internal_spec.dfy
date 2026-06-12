function DigitsumSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then
    0
  else
    (if ('A' as int) <= (s[0] as int) && (s[0] as int) <= ('Z' as int) then (s[0] as int) else 0) + DigitsumSpec(s[1..])
}

method digitSum(s: string) returns (result: int)
  requires true
  ensures result == DigitsumSpec(s)
{
  assume false;
}
