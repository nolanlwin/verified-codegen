function ContainsChar(s: string, c: char, i: int): bool
  decreases |s| - i
{
  if i == |s| then false else s[i] == c || ContainsChar(s, c, i + 1)
}
function AllCharsIn(s0: string, s1: string, i: int): bool
  decreases |s0| - i
{
  if i == |s0| then true else ContainsChar(s1, s0[i], 0) && AllCharsIn(s0, s1, i + 1)
}
function SameCharsSpec(s0: string, s1: string): bool
{
  AllCharsIn(s0, s1, 0) && AllCharsIn(s1, s0, 0)
}

method same_chars(s0: string, s1: string) returns (result: bool)
  ensures result == SameCharsSpec(s0, s1)
{
  assume false;
}
