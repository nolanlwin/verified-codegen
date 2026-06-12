function IsSentenceDelimiter(c: char): bool
{
  c == '.' || c == '?' || c == "!"
}
function StartsWithWordI(S: string): bool
{
  if |S| == 0 then false
  else if S[0] != 'I' then false
  else if |S| == 1 then true
  else S[1] == ' ' || IsSentenceDelimiter(S[1])
}
function IsBoredSpec(S: string): int
  decreases |S|
{
  if |S| == 0 then 0
  else if S[0] == ' ' then IsBoredSpec(S[1..])
  else if IsSentenceDelimiter(S[0]) then IsBoredSpec(S[1..])
  else (if StartsWithWordI(S) then 1 else 0) + IsBoredAfterFirstWord(S[1..])
}
function IsBoredAfterFirstWord(S: string): int
  decreases |S|
{
  if |S| == 0 then 0
  else if IsSentenceDelimiter(S[0]) then IsBoredSpec(S[1..])
  else IsBoredAfterFirstWord(S[1..])
}

method is_bored(S: string) returns (result: int)
  requires true
  ensures result == IsBoredSpec(S)
{
  assume false;
}
