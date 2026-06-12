function IsDigit(c: char): bool
{
  '0' <= c && c <= '9'
}

function IsLatinLetter(c: char): bool
{
  ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z')
}

function CountDigits(s: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else (if IsDigit(s[0]) then 1 else 0) + CountDigits(s[1..])
}

function CountDots(s: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else (if s[0] == '.' then 1 else 0) + CountDots(s[1..])
}

function ExtensionMatches(s: string, start: int): bool
{
  s[start..] == "txt" || s[start..] == "exe" || s[start..] == "dll"
}

function HasValidDotAndExtensionFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then false
  else if s[i] == '.' then i > 0 && IsLatinLetter(s[0]) && ExtensionMatches(s, i + 1)
  else HasValidDotAndExtensionFrom(s, i + 1)
}

function FileNameCheckSpec(file_name: string): string
{
  if CountDigits(file_name) <= 3 && CountDots(file_name) == 1 && HasValidDotAndExtensionFrom(file_name, 0) then "Yes"
  else "No"
}

method file_name_check(file_name: string) returns (result: string)
  ensures result == FileNameCheckSpec(file_name)
{
  result := FileNameCheckSpec(file_name);
}
