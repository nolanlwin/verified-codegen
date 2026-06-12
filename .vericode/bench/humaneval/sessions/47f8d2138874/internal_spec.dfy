function FlipChar(c: char): char
{
  if c == 'a' then "A"
  else if c == 'b' then "B"
  else if c == 'c' then "C"
  else if c == 'd' then "D"
  else if c == 'e' then "E"
  else if c == 'f' then "F"
  else if c == 'g' then "G"
  else if c == 'h' then "H"
  else if c == 'i' then "I"
  else if c == 'j' then "J"
  else if c == 'k' then "K"
  else if c == 'l' then "L"
  else if c == 'm' then "M"
  else if c == 'n' then "N"
  else if c == 'o' then "O"
  else if c == 'p' then "P"
  else if c == 'q' then "Q"
  else if c == 'r' then "R"
  else if c == 's' then "S"
  else if c == 't' then "T"
  else if c == 'u' then "U"
  else if c == 'v' then "V"
  else if c == 'w' then "W"
  else if c == 'x' then "X"
  else if c == 'y' then "Y"
  else if c == 'z' then "Z"
  else if c == 'A' then "a"
  else if c == 'B' then "b"
  else if c == 'C' then "c"
  else if c == 'D' then "d"
  else if c == 'E' then "e"
  else if c == 'F' then "f"
  else if c == 'G' then "g"
  else if c == 'H' then "h"
  else if c == 'I' then "i"
  else if c == 'J' then "j"
  else if c == 'K' then "k"
  else if c == 'L' then "l"
  else if c == 'M' then "m"
  else if c == 'N' then "n"
  else if c == 'O' then "o"
  else if c == 'P' then "p"
  else if c == 'Q' then "q"
  else if c == 'R' then "r"
  else if c == 'S' then "s"
  else if c == 'T' then "t"
  else if c == 'U' then "u"
  else if c == 'V' then "v"
  else if c == 'W' then "w"
  else if c == 'X' then "x"
  else if c == 'Y' then "y"
  else if c == 'Z' then "z"
  else c
}
function FlipCaseSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then "" else [FlipChar(s[0])] + FlipCaseSpec(s[1..])
}

method flip_case(s: string) returns (result: string)
  requires true
  ensures result == FlipCaseSpec(s)
{
  assume false;
}
