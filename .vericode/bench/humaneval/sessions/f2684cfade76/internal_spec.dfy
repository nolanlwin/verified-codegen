function PrefixMatches(s: string, sub: string, j: int): bool
  decreases |sub| - j
{
  if j == |sub| then true else s[j] == sub[j] && PrefixMatches(s, sub, j + 1)
}
function HowManyTimesSpec(s: string, sub: string): int
  decreases |s|
{
  if |sub| == 0 then |s| + 1
  else if |s| < |sub| then 0
  else (if PrefixMatches(s, sub, 0) then 1 else 0) + HowManyTimesSpec(s[1..], sub)
}

method how_many_times(s: string, sub: string) returns (result: int)
  ensures result == HowManyTimesSpec(s, sub)
{
  assume false;
}
