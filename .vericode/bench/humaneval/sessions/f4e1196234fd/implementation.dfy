function LowerAscii(c: char): char
{
  if c == "A"[0] then "a"[0]
  else if c == "B"[0] then "b"[0]
  else if c == "C"[0] then "c"[0]
  else if c == "D"[0] then "d"[0]
  else if c == "E"[0] then "e"[0]
  else if c == "F"[0] then "f"[0]
  else if c == "G"[0] then "g"[0]
  else if c == "H"[0] then "h"[0]
  else if c == "I"[0] then "i"[0]
  else if c == "J"[0] then "j"[0]
  else if c == "K"[0] then "k"[0]
  else if c == "L"[0] then "l"[0]
  else if c == "M"[0] then "m"[0]
  else if c == "N"[0] then "n"[0]
  else if c == "O"[0] then "o"[0]
  else if c == "P"[0] then "p"[0]
  else if c == "Q"[0] then "q"[0]
  else if c == "R"[0] then "r"[0]
  else if c == "S"[0] then "s"[0]
  else if c == "T"[0] then "t"[0]
  else if c == "U"[0] then "u"[0]
  else if c == "V"[0] then "v"[0]
  else if c == "W"[0] then "w"[0]
  else if c == "X"[0] then "x"[0]
  else if c == "Y"[0] then "y"[0]
  else if c == "Z"[0] then "z"[0]
  else c
}

function SameCharacterIgnoringCase(a: char, b: char): bool
{
  LowerAscii(a) == LowerAscii(b)
}

function ContainsEquivalentCharacter(s: string, c: char): bool
  decreases |s|
{
  if |s| == 0 then
    false
  else
    SameCharacterIgnoringCase(s[0], c) || ContainsEquivalentCharacter(s[1..], c)
}

function CountDistinctCharactersSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then
    0
  else
    (if ContainsEquivalentCharacter(s[1..], s[0]) then 0 else 1) + CountDistinctCharactersSpec(s[1..])
}

method count_distinct_characters(s: string) returns (result: int)
  requires true
  ensures result == CountDistinctCharactersSpec(s)
  decreases |s|
{
  if |s| == 0 {
    result := 0;
  } else {
    var tailResult := count_distinct_characters(s[1..]);
    if ContainsEquivalentCharacter(s[1..], s[0]) {
      result := tailResult;
    } else {
      result := 1 + tailResult;
    }
  }
}
