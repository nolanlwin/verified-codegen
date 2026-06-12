datatype Key = Str(s: string) | NonString
function IsLowerChar(c: char): bool
{
  c == 'a' || c == 'b' || c == 'c' || c == 'd' || c == 'e' || c == 'f' ||
  c == 'g' || c == 'h' || c == 'i' || c == 'j' || c == 'k' || c == 'l' ||
  c == 'm' || c == 'n' || c == 'o' || c == 'p' || c == 'q' || c == 'r' ||
  c == 's' || c == 't' || c == 'u' || c == 'v' || c == 'w' || c == 'x' ||
  c == 'y' || c == "z"
}
function IsUpperChar(c: char): bool
{
  c == 'A' || c == 'B' || c == 'C' || c == 'D' || c == 'E' || c == 'F' ||
  c == 'G' || c == 'H' || c == 'I' || c == 'J' || c == 'K' || c == 'L' ||
  c == 'M' || c == 'N' || c == 'O' || c == 'P' || c == 'Q' || c == 'R' ||
  c == 'S' || c == 'T' || c == 'U' || c == 'V' || c == 'W' || c == 'X' ||
  c == 'Y' || c == "Z"
}
function AllLowerCharsFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then true else IsLowerChar(s[i]) && AllLowerCharsFrom(s, i + 1)
}
function AllUpperCharsFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then true else IsUpperChar(s[i]) && AllUpperCharsFrom(s, i + 1)
}
function IsLowerString(s: string): bool
{
  |s| > 0 && AllLowerCharsFrom(s, 0)
}
function IsUpperString(s: string): bool
{
  |s| > 0 && AllUpperCharsFrom(s, 0)
}
function AllKeysLowerFrom(keys: seq<Key>, i: int): bool
  decreases |keys| - i
{
  if i == |keys| then true else
    match keys[i]
    case Str(s) => IsLowerString(s) && AllKeysLowerFrom(keys, i + 1)
    case NonString => false
}
function AllKeysUpperFrom(keys: seq<Key>, i: int): bool
  decreases |keys| - i
{
  if i == |keys| then true else
    match keys[i]
    case Str(s) => IsUpperString(s) && AllKeysUpperFrom(keys, i + 1)
    case NonString => false
}
function CheckDictCaseSpec(keys: seq<Key>): bool
{
  if |keys| == 0 then false else AllKeysLowerFrom(keys, 0) || AllKeysUpperFrom(keys, 0)
}

method check_dict_case(keys: seq<Key>) returns (result: bool)
  requires true
  ensures result == CheckDictCaseSpec(keys)
{
  assume false;
}
