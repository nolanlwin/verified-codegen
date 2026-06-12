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
  decreases |s|
{
  if |s| == 0 {
    result := "";
  } else if s[0] == " "[0] {
    var tail := anti_shuffle(s[1..]);
    result := " " + tail;
  } else {
    var tail := anti_shuffle(s[1..]);
    result := InsertIntoFirstWordMethod(s[0], tail);
  }
}

method InsertIntoFirstWordMethod(c: char, t: string) returns (result: string)
  ensures result == InsertIntoFirstWord(c, t)
  decreases |t|
{
  if |t| == 0 {
    result := [c];
  } else if t[0] == " "[0] {
    result := [c] + t;
  } else if (c as int) <= (t[0] as int) {
    result := [c] + t;
  } else {
    var rest := InsertIntoFirstWordMethod(c, t[1..]);
    result := [t[0]] + rest;
  }
}
