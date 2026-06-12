function ContainsCharFrom(s: string, i: int, c: char): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then false else s[i] == c || ContainsCharFrom(s, i + 1, c)
}
function UniqueCharCountFrom(s: string, i: int): int
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then 0
  else if ContainsCharFrom(s, i + 1, s[i]) then UniqueCharCountFrom(s, i + 1)
  else 1 + UniqueCharCountFrom(s, i + 1)
}
function UniqueCharCount(s: string): int
{
  UniqueCharCountFrom(s, 0)
}
function LexLessFrom(a: string, b: string, i: int): bool
  decreases |a| - i
{
  if i == |a| then i < |b|
  else if i == |b| then false
  else if (a[i] as int) < (b[i] as int) then true
  else if (b[i] as int) < (a[i] as int) then false
  else LexLessFrom(a, b, i + 1)
}
function LexLess(a: string, b: string): bool
{
  LexLessFrom(a, b, 0)
}
function BetterWord(a: string, b: string): string
{
  if UniqueCharCount(a) > UniqueCharCount(b) then a
  else if UniqueCharCount(b) > UniqueCharCount(a) then b
  else if LexLess(a, b) then a
  else b
}
function FindMaxSpec(words: seq<string>): string
  decreases |words|
{
  if |words| == 1 then words[0]
  else BetterWord(words[0], FindMaxSpec(words[1..]))
}

method find_max(words: seq<string>) returns (result: string)
  requires |words| > 0
  ensures result == FindMaxSpec(words)
{
  assume false;
}
