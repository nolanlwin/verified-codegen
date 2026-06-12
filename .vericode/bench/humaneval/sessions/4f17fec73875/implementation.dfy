function StartsWithAt(s: string, substring: string, i: int, j: int): bool
  decreases |substring| - j
{
  if j == |substring| then
    true
  else
    s[i] == substring[j] && StartsWithAt(s, substring, i + 1, j + 1)
}

function ContainsSubstringFrom(s: string, substring: string, i: int): bool
  decreases |s| - i
{
  if |substring| == 0 then
    true
  else if i + |substring| > |s| then
    false
  else if StartsWithAt(s, substring, i, 0) then
    true
  else
    ContainsSubstringFrom(s, substring, i + 1)
}

function ContainsSubstring(s: string, substring: string): bool
{
  ContainsSubstringFrom(s, substring, 0)
}

function FilterBySubstringSpec(strings: seq<string>, substring: string): seq<string>
  decreases |strings|
{
  if |strings| == 0 then
    []
  else if ContainsSubstring(strings[0], substring) then
    [strings[0]] + FilterBySubstringSpec(strings[1..], substring)
  else
    FilterBySubstringSpec(strings[1..], substring)
}

method filter_by_substring(strings: seq<string>, substring: string) returns (result: seq<string>)
  ensures result == FilterBySubstringSpec(strings, substring)
  decreases |strings|
{
  if |strings| == 0 {
    result := [];
  } else {
    var rest := filter_by_substring(strings[1..], substring);
    if ContainsSubstring(strings[0], substring) {
      result := [strings[0]] + rest;
    } else {
      result := rest;
    }
  }
}
