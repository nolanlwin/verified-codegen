function IsVowel(c: char): bool
{
  c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
  c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
}

function CountConsonantsSpec(w: string): int
  decreases |w|
{
  if |w| == 0 then 0
  else
    (if w[0] == ' ' || IsVowel(w[0]) then 0 else 1) + CountConsonantsSpec(w[1..])
}

function KeepWordSpec(w: string, n: int): seq<string>
{
  if |w| > 0 && CountConsonantsSpec(w) == n then [w] else []
}

function SelectWordsAux(s: string, n: int, current: string): seq<string>
  decreases |s|
{
  if |s| == 0 then KeepWordSpec(current, n)
  else if s[0] == ' ' then KeepWordSpec(current, n) + SelectWordsAux(s[1..], n, "")
  else SelectWordsAux(s[1..], n, current + s[..1])
}

function SelectWordsSpec(s: string, n: int): seq<string>
{
  SelectWordsAux(s, n, "")
}

method select_words(s: string, n: int) returns (result: seq<string>)
  requires n >= 0
  ensures result == SelectWordsSpec(s, n)
{
  result := SelectWordsAuxMethod(s, n, "");
}

method SelectWordsAuxMethod(s: string, n: int, current: string) returns (result: seq<string>)
  ensures result == SelectWordsAux(s, n, current)
  decreases |s|
{
  if |s| == 0 {
    if |current| > 0 && CountConsonantsSpec(current) == n {
      result := [current];
    } else {
      result := [];
    }
    assert result == KeepWordSpec(current, n);
  } else if s[0] == ' ' {
    var kept: seq<string>;
    if |current| > 0 && CountConsonantsSpec(current) == n {
      kept := [current];
    } else {
      kept := [];
    }
    assert kept == KeepWordSpec(current, n);
    var rest := SelectWordsAuxMethod(s[1..], n, "");
    result := kept + rest;
  } else {
    result := SelectWordsAuxMethod(s[1..], n, current + s[..1]);
  }
}
