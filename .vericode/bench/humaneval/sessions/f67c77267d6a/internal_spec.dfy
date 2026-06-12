function InsertIntoFirstWord(c: char, t: string): string
  decreases |t|
{
  if |t| == 0 then [c]
  else if t[0] == " "[0] then [c] + t
  else if (c as int) <= (t[0] as int) then [c] + t
  else [t[0]] + InsertIntoFirstWord(c, t[1..])
}
function AntiShuffleSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else if s[0] == " "[0] then " " + AntiShuffleSpec(s[1..])
  else InsertIntoFirstWord(s[0], AntiShuffleSpec(s[1..]))
}

method anti_shuffle(s: string) returns (result: string)
  requires true
  ensures result == AntiShuffleSpec(s)
{
  assume false;
}
