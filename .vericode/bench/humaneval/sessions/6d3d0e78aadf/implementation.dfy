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
  if i <= 0 || i >= |word| - 1 then ""
  else if IsVowel(word[i]) && IsConsonant(word[i - 1]) && IsConsonant(word[i + 1]) then word[i..i + 1]
  else GetClosestVowelAux(word, i - 1)
}

function GetClosestVowelSpec(word: string): string
{
  if |word| < 3 then ""
  else GetClosestVowelAux(word, |word| - 2)
}

method get_closest_vowel(word: string) returns (result: string)
  ensures result == GetClosestVowelSpec(word)
{
  if |word| < 3 {
    result := "";
  } else {
    result := GetClosestVowelAuxMethod(word, |word| - 2);
  }
}

method GetClosestVowelAuxMethod(word: string, i: int) returns (res: string)
  ensures res == GetClosestVowelAux(word, i)
  decreases if i <= 0 then 0 else i
{
  if i <= 0 || i >= |word| - 1 {
    res := "";
  } else if IsVowel(word[i]) && IsConsonant(word[i - 1]) && IsConsonant(word[i + 1]) {
    res := word[i..i + 1];
  } else {
    res := GetClosestVowelAuxMethod(word, i - 1);
  }
}
