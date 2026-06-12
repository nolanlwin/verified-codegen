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
  assume false;
}
