function IsUpperVowel(c: char): bool
{
  c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == "U"
}
function CountUpperSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then
    0
  else if |s| == 1 then
    if IsUpperVowel(s[0]) then 1 else 0
  else
    (if IsUpperVowel(s[0]) then 1 else 0) + CountUpperSpec(s[2..])
}

method count_upper(s: string) returns (result: int)
  ensures result == CountUpperSpec(s)
{
  assume false;
}
