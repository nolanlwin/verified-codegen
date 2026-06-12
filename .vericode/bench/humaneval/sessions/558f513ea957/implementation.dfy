function IsWordsStringDelimiter(c: char): bool
{
  c == ' ' || c == ','
}

function IsSeparator(c: char): bool
{
  c == ' ' || c == ','
}

function WordsStringAcc(s: string, i: int, current: string): seq<string>
  requires 0 <= i <= |s|
  decreases |s| - i
{
  if i == |s| then
    if |current| == 0 then [] else [current]
  else if IsSeparator(s[i]) then
    if |current| == 0 then WordsStringAcc(s, i + 1, "")
    else [current] + WordsStringAcc(s, i + 1, "")
  else
    WordsStringAcc(s, i + 1, current + [s[i]])
}

function WordsStringSpec(s: string): seq<string>
{
  WordsStringAcc(s, 0, "")
}

method words_string(s: string) returns (result: seq<string>)
  ensures result == WordsStringSpec(s)
{
  result := WordsStringAccMethod(s, 0, "");
}
method WordsStringAccMethod(s: string, i: int, current: string) returns (result: seq<string>)
  requires 0 <= i <= |s|
  ensures result == WordsStringAcc(s, i, current)
  decreases |s| - i
{
  if i == |s| {
    if |current| == 0 { result := []; } else { result := [current]; }
  } else if IsSeparator(s[i]) {
    if |current| == 0 {
      result := WordsStringAccMethod(s, i + 1, "");
    } else {
      var rest := WordsStringAccMethod(s, i + 1, "");
      result := [current] + rest;
    }
  } else {
    result := WordsStringAccMethod(s, i + 1, current + [s[i]]);
  }
}
