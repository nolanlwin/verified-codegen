function IsRegularVowel(c: char): bool
{
  c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
  c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == "U"
}
function IsY(c: char): bool
{
  c == 'y' || c == "Y"
}
function VowelsCountAux(s: string, i: int): int
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then
    0
  else
    (if IsRegularVowel(s[i]) || (i == |s| - 1 && IsY(s[i])) then 1 else 0) + VowelsCountAux(s, i + 1)
}
function VowelsCountSpec(s: string): int
{
  VowelsCountAux(s, 0)
}

method vowels_count(s: string) returns (result: int)
  ensures result == VowelsCountSpec(s)
{
  assume false;
}
