function ParseNestedParensSpec(paren_string: string, i: int, currentDepth: int, currentMax: int, inGroup: bool): seq<int>
  decreases |paren_string| - i
{
  if i == |paren_string| then
    if inGroup then [currentMax] else []
  else if paren_string[i..i+1] == " " then
    if inGroup then [currentMax] + ParseNestedParensSpec(paren_string, i + 1, 0, 0, false)
    else ParseNestedParensSpec(paren_string, i + 1, 0, 0, false)
  else if paren_string[i..i+1] == "(" then
    var nextDepth := currentDepth + 1;
    var nextMax := if currentMax < nextDepth then nextDepth else currentMax;
    ParseNestedParensSpec(paren_string, i + 1, nextDepth, nextMax, true)
  else if paren_string[i..i+1] == ")" then
    ParseNestedParensSpec(paren_string, i + 1, currentDepth - 1, currentMax, true)
  else
    ParseNestedParensSpec(paren_string, i + 1, currentDepth, currentMax, true)
}

method parse_nested_parens(paren_string: string) returns (result: seq<int>)
  requires true
  ensures result == ParseNestedParensSpec(paren_string, 0, 0, 0, false)
{
  result := ParseNestedParensAux(paren_string, 0, 0, 0, false);
}

method ParseNestedParensAux(paren_string: string, i: int, currentDepth: int, currentMax: int, inGroup: bool) returns (result: seq<int>)
  requires 0 <= i <= |paren_string|
  ensures result == ParseNestedParensSpec(paren_string, i, currentDepth, currentMax, inGroup)
  decreases |paren_string| - i
{
  if i == |paren_string| {
    if inGroup {
      result := [currentMax];
    } else {
      result := [];
    }
  } else if paren_string[i..i+1] == " " {
    var tail := ParseNestedParensAux(paren_string, i + 1, 0, 0, false);
    if inGroup {
      result := [currentMax] + tail;
    } else {
      result := tail;
    }
  } else if paren_string[i..i+1] == "(" {
    var nextDepth := currentDepth + 1;
    var nextMax := if currentMax < nextDepth then nextDepth else currentMax;
    result := ParseNestedParensAux(paren_string, i + 1, nextDepth, nextMax, true);
  } else if paren_string[i..i+1] == ")" {
    result := ParseNestedParensAux(paren_string, i + 1, currentDepth - 1, currentMax, true);
  } else {
    result := ParseNestedParensAux(paren_string, i + 1, currentDepth, currentMax, true);
  }
}
