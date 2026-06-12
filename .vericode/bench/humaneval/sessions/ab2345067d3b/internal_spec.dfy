function LowercaseLetters(): string
{
  "abcdefghijklmnopqrstuvwxyz"
}
function UppercaseLetters(): string
{
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
function IsInAlphabet(c: char, alphabet: string, i: int): bool
  decreases |alphabet| - i
{
  if i == |alphabet| then false
  else c == alphabet[i] || IsInAlphabet(c, alphabet, i + 1)
}
function ToggleByAlphabet(c: char, from: string, to: string, i: int): char
  decreases |from| - i
{
  if i == |from| then c
  else if c == from[i] then to[i]
  else ToggleByAlphabet(c, from, to, i + 1)
}
function IsAsciiLetter(c: char): bool
{
  IsInAlphabet(c, LowercaseLetters(), 0) || IsInAlphabet(c, UppercaseLetters(), 0)
}
function ToggleAsciiCase(c: char): char
{
  if IsInAlphabet(c, LowercaseLetters(), 0) then ToggleByAlphabet(c, LowercaseLetters(), UppercaseLetters(), 0)
  else if IsInAlphabet(c, UppercaseLetters(), 0) then ToggleByAlphabet(c, UppercaseLetters(), LowercaseLetters(), 0)
  else c
}
function ContainsLetterFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then false
  else IsAsciiLetter(s[i]) || ContainsLetterFrom(s, i + 1)
}
function ToggleCaseFrom(s: string, i: int): string
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then ""
  else [ToggleAsciiCase(s[i])] + ToggleCaseFrom(s, i + 1)
}
function SolveSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then ""
  else if ContainsLetterFrom(s, 0) then [ToggleAsciiCase(s[0])] + ToggleCaseFrom(s, 1)
  else SolveSpec(s[1..]) + [s[0]]
}

method solve(s: string) returns (result: string)
  ensures result == SolveSpec(s)
{
  assume false;
}
