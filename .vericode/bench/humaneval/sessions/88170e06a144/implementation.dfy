function IsPalindromeSpec(text: string): bool
  decreases |text|
{
  if |text| <= 1 then
    true
  else
    text[0] == text[|text| - 1] && IsPalindromeSpec(text[1..|text| - 1])
}

method is_palindrome(text: string) returns (result: bool)
  ensures result == IsPalindromeSpec(text)
  decreases |text|
{
  if |text| <= 1 {
    result := true;
  } else if text[0] != text[|text| - 1] {
    result := false;
  } else {
    result := is_palindrome(text[1..|text| - 1]);
  }
}
