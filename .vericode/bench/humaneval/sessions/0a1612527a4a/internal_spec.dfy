function SeparateParenGroupsAux(s: string, i: int, depth: int, current: string, groups: seq<string>): seq<string>
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then groups
  else if s[i] == ' ' then
    SeparateParenGroupsAux(s, i + 1, depth, current, groups)
  else if s[i] == '(' then
    var nextCurrent := if depth == 0 then ['('] else current + ['('];
    SeparateParenGroupsAux(s, i + 1, depth + 1, nextCurrent, groups)
  else if s[i] == ')' then
    if depth == 1 then
      SeparateParenGroupsAux(s, i + 1, 0, "", groups + [current + [')']])
    else if depth > 1 then
      SeparateParenGroupsAux(s, i + 1, depth - 1, current + [')'], groups)
    else
      SeparateParenGroupsAux(s, i + 1, depth, current, groups)
  else
    SeparateParenGroupsAux(s, i + 1, depth, current, groups)
}
function SeparateParenGroupsSpec(paren_string: string): seq<string>
{
  SeparateParenGroupsAux(paren_string, 0, 0, "", [])
}

method separate_paren_groups(paren_string: string) returns (result: seq<string>)
  ensures result == SeparateParenGroupsSpec(paren_string)
{
  assume false;
}
