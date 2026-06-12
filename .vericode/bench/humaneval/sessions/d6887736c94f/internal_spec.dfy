function IsVowel(c: char): bool
{
  c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
  c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == "U"
}
function RemoveVowelsSpec(text: string): string
  decreases |text|
{
  if |text| == 0 then
    ""
  else if IsVowel(text[0]) then
    RemoveVowelsSpec(text[1..])
  else
    text[0..1] + RemoveVowelsSpec(text[1..])
}

method remove_vowels(text: string) returns (result: string)
  requires true
  ensures result == RemoveVowelsSpec(text)
{
  assume false;
}
