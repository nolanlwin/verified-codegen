function ContainsCharSpec(chars: string, ch: char): bool
  decreases |chars|
{
  if |chars| == 0 then false
  else chars[0] == ch || ContainsCharSpec(chars[1..], ch)
}

function DeleteCharsSpec(s: string, c: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else if ContainsCharSpec(c, s[0]) then DeleteCharsSpec(s[1..], c)
  else [s[0]] + DeleteCharsSpec(s[1..], c)
}

function IsPalindromeSpec(s: string): bool
  decreases |s|
{
  if |s| <= 1 then true
  else s[0] == s[|s| - 1] && IsPalindromeSpec(s[1..|s| - 1])
}

function ReverseDeleteSpec(s: string, c: string): (string, bool)
{
  var filtered := DeleteCharsSpec(s, c);
  (filtered, IsPalindromeSpec(filtered))
}

method reverse_delete(s: string, c: string) returns (result: (string, bool))
  ensures result == ReverseDeleteSpec(s, c)
{
  result := ReverseDeleteSpec(s, c);
}
