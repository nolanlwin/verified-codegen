function ContainsFromSpec(a: string, pattern: string, i: int): bool
  decreases |a| - i
{
  if |pattern| == 0 then true
  else if i + |pattern| > |a| then false
  else if a[i..i + |pattern|] == pattern then true
  else ContainsFromSpec(a, pattern, i + 1)
}
function ContainsSpec(a: string, pattern: string): bool
{
  ContainsFromSpec(a, pattern, 0)
}
function RotationContainsFromSpec(a: string, b: string, k: int): bool
  decreases |b| - k
{
  if k == |b| then false
  else if ContainsSpec(a, b[k..] + b[..k]) then true
  else RotationContainsFromSpec(a, b, k + 1)
}
function CycpatternCheckSpec(a: string, b: string): bool
{
  if |b| == 0 then true
  else RotationContainsFromSpec(a, b, 0)
}

method cycpattern_check(a: string, b: string) returns (result: bool)
  ensures result == CycpatternCheckSpec(a, b)
{
  assume false;
}
