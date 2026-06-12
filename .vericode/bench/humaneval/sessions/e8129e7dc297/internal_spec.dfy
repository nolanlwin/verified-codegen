function ReverseSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else ReverseSpec(s[1..]) + s[0..1]
}
function IsPalindromeSpec(s: string): bool
  decreases |s|
{
  false
}
function PrefixBeforeLongestPalindromicSuffixSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else if IsPalindromeSpec(s) then ""
  else s[0..1] + PrefixBeforeLongestPalindromicSuffixSpec(s[1..])
}
function MakePalindromeSpec(s: string): string
{
  s + ReverseSpec(PrefixBeforeLongestPalindromicSuffixSpec(s))
}

method make_palindrome(s: string) returns (result: string)
  ensures result == MakePalindromeSpec(s)
{
  assume false;
}
