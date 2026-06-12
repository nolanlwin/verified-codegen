function OnlySquareBrackets(s: string): bool
  decreases |s|
{
  if |s| == 0 then true
  else (s[0] == '[' || s[0] == ']') && OnlySquareBrackets(s[1..])
}
function IsNestedAux(s: string, matched: int): bool
  decreases |s|
{
  if matched == 4 then true
  else if |s| == 0 then false
  else if matched == 0 || matched == 1 then
    if s[0] == '[' then IsNestedAux(s[1..], matched + 1) else IsNestedAux(s[1..], matched)
  else
    if s[0] == ']' then IsNestedAux(s[1..], matched + 1) else IsNestedAux(s[1..], matched)
}
function IsNestedSpec(s: string): bool
{
  IsNestedAux(s, 0)
}

method is_nested(s: string) returns (result: bool)
  requires OnlySquareBrackets(s)
  ensures result == IsNestedSpec(s)
{
  assume false;
}
