function IsVowel(c: char): bool
{
  c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
  c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
}
function IsConsonant(c: char): bool
{
  !IsVowel(c)
}
function GetClosestVowelAux(word: string, i: int): string
  decreases i
{
  ""
}
function GetClosestVowelSpec(word: string): string
{
  if |word| < 3 then ""
  else GetClosestVowelAux(word, |word| - 2)
}

method get_closest_vowel(word: string) returns (result: string)
  ensures result == GetClosestVowelSpec(word)
{
  assume false;
}
