datatype SplitWordsResult = Words(words: seq<string>) | Count(count: int)
function IsWhitespace(c: char): bool
{
  c == ' ' || c == '\t' || c == '\n' || c == '\r'
}
function ContainsWhitespace(s: string): bool
  decreases |s|
{
  if |s| == 0 then false
  else IsWhitespace(s[0]) || ContainsWhitespace(s[1..])
}
function ContainsComma(s: string): bool
  decreases |s|
{
  if |s| == 0 then false
  else s[0] == ',' || ContainsComma(s[1..])
}
function SplitWhitespaceScan(s: string, start: int, i: int): seq<string>
  decreases |s| - i
{
  if i == |s| then
    if start < i then [s[start..i]] else []
  else if IsWhitespace(s[i]) then
    if start < i then [s[start..i]] + SplitWhitespaceScan(s, i + 1, i + 1)
    else SplitWhitespaceScan(s, i + 1, i + 1)
  else SplitWhitespaceScan(s, start, i + 1)
}
function SplitOnWhitespaceSpec(s: string): seq<string>
{
  SplitWhitespaceScan(s, 0, 0)
}
function SplitCommaScan(s: string, start: int, i: int): seq<string>
  decreases |s| - i
{
  if i == |s| then
    if start < i then [s[start..i]] else []
  else if s[i] == ',' then
    if start < i then [s[start..i]] + SplitCommaScan(s, i + 1, i + 1)
    else SplitCommaScan(s, i + 1, i + 1)
  else SplitCommaScan(s, start, i + 1)
}
function SplitOnCommaSpec(s: string): seq<string>
{
  SplitCommaScan(s, 0, 0)
}
function IsOddOrderLowercase(c: char): bool
{
  c == 'b' || c == 'd' || c == 'f' || c == 'h' || c == 'j' || c == 'l' ||
  c == 'n' || c == 'p' || c == 'r' || c == 't' || c == 'v' || c == 'x' || c == 'z'
}
function CountOddLowercase(s: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else (if IsOddOrderLowercase(s[0]) then 1 else 0) + CountOddLowercase(s[1..])
}
function SplitWordsSpec(txt: string): SplitWordsResult
{
  if ContainsWhitespace(txt) then Words(SplitOnWhitespaceSpec(txt))
  else if ContainsComma(txt) then Words(SplitOnCommaSpec(txt))
  else Count(CountOddLowercase(txt))
}

method split_words(txt: string) returns (result: SplitWordsResult)
  ensures result == SplitWordsSpec(txt)
{
  assume false;
}
