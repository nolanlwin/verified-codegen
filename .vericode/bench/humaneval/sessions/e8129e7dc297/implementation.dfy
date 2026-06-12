function ReverseSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else ReverseSpec(s[1..]) + s[0..1]
}

function IsPalindromeSpec(s: string): bool
  decreases |s|
{
  s == ReverseSpec(s)
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
  var prefix := PrefixBeforeLongestPalindromicSuffixImpl(s);
  var reversedPrefix := ReverseImpl(prefix);
  result := s + reversedPrefix;
}

method ReverseImpl(s: string) returns (r: string)
  ensures r == ReverseSpec(s)
  decreases |s|
{
  if |s| == 0 {
    r := "";
  } else {
    var t := ReverseImpl(s[1..]);
    r := t + s[0..1];
  }
}

method PrefixBeforeLongestPalindromicSuffixImpl(s: string) returns (p: string)
  ensures p == PrefixBeforeLongestPalindromicSuffixSpec(s)
  decreases |s|
{
  if |s| == 0 {
    p := "";
  } else if IsPalindromeSpec(s) {
    p := "";
  } else {
    var q := PrefixBeforeLongestPalindromicSuffixImpl(s[1..]);
    p := s[0..1] + q;
  }
}
