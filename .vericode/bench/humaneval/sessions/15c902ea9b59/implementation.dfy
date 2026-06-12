function IsAsciiLetter(c: char): bool
{
  ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z')
}

function CheckIfLastCharIsALetterSpec(txt: string): bool
  decreases |txt|
{
  if |txt| == 0 then false
  else if |txt| == 1 then IsAsciiLetter(txt[0])
  else if |txt| == 2 then IsAsciiLetter(txt[1]) && txt[0] == ' '
  else CheckIfLastCharIsALetterSpec(txt[1..])
}

method check_if_last_char_is_a_letter(txt: string) returns (result: bool)
  ensures result == CheckIfLastCharIsALetterSpec(txt)
  decreases |txt|
{
  if |txt| == 0 {
    result := false;
  } else if |txt| == 1 {
    result := IsAsciiLetter(txt[0]);
  } else if |txt| == 2 {
    result := IsAsciiLetter(txt[1]) && txt[0] == ' ';
  } else {
    result := check_if_last_char_is_a_letter(txt[1..]);
  }
}
