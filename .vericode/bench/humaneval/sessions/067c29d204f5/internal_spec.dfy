function ValidMusicFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then true
  else if s[i] == ' ' then ValidMusicFrom(s, i + 1)
  else if s[i] == 'o' then
    if i + 1 < |s| && s[i + 1] == '|' then
      (i + 2 == |s| || s[i + 2] == " ") && ValidMusicFrom(s, i + 2)
    else
      (i + 1 == |s| || s[i + 1] == " ") && ValidMusicFrom(s, i + 1)
  else if s[i] == '.' then
    i + 1 < |s| && s[i + 1] == '|' && (i + 2 == |s| || s[i + 2] == " ") && ValidMusicFrom(s, i + 2)
  else false
}
function ValidMusicString(s: string): bool
{
  ValidMusicFrom(s, 0)
}
function ParseMusicFrom(s: string, i: int): seq<int>
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then []
  else if s[i] == ' ' then ParseMusicFrom(s, i + 1)
  else if s[i] == 'o' && i + 1 < |s| && s[i + 1] == '|' then [2] + ParseMusicFrom(s, i + 2)
  else if s[i] == 'o' then [4] + ParseMusicFrom(s, i + 1)
  else if s[i] == '.' && i + 1 < |s| && s[i + 1] == '|' then [1] + ParseMusicFrom(s, i + 2)
  else ParseMusicFrom(s, i + 1)
}
function ParseMusicSpec(music_string: string): seq<int>
{
  ParseMusicFrom(music_string, 0)
}

method parse_music(music_string: string) returns (result: seq<int>)
  requires ValidMusicString(music_string)
  ensures result == ParseMusicSpec(music_string)
{
  assume false;
}
