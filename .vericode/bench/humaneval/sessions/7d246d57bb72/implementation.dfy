function IsParenString(s: string): bool
  decreases |s|
{
  if |s| == 0 then true
  else (s[0] == '(' || s[0] == ')') && IsParenString(s[1..])
}

function IsGoodParensAux(s: string, balance: int): bool
  decreases |s|
{
  if |s| == 0 then balance == 0
  else if s[0] == '(' then IsGoodParensAux(s[1..], balance + 1)
  else if s[0] == ')' then balance > 0 && IsGoodParensAux(s[1..], balance - 1)
  else false
}

function IsGoodParens(s: string): bool
{
  IsGoodParensAux(s, 0)
}

function MatchParensSpec(lst: seq<string>): string
{
  if IsGoodParens(lst[0] + lst[1]) || IsGoodParens(lst[1] + lst[0]) then "Yes" else "No"
}

method match_parens(lst: seq<string>) returns (result: string)
  requires |lst| == 2
  requires IsParenString(lst[0])
  requires IsParenString(lst[1])
  ensures result == MatchParensSpec(lst)
{
  var first := lst[0] + lst[1];
  var second := lst[1] + lst[0];

  var okFirst := ComputeIsGoodParens(first);
  if okFirst {
    result := "Yes";
  } else {
    var okSecond := ComputeIsGoodParens(second);
    if okSecond {
      result := "Yes";
    } else {
      result := "No";
    }
  }
}

method ComputeIsGoodParensAux(s: string, balance: int) returns (r: bool)
  ensures r == IsGoodParensAux(s, balance)
  decreases |s|
{
  if |s| == 0 {
    r := balance == 0;
  } else if s[0] == '(' {
    r := ComputeIsGoodParensAux(s[1..], balance + 1);
  } else if s[0] == ')' {
    if balance > 0 {
      r := ComputeIsGoodParensAux(s[1..], balance - 1);
    } else {
      r := false;
    }
  } else {
    r := false;
  }
}

method ComputeIsGoodParens(s: string) returns (r: bool)
  ensures r == IsGoodParens(s)
{
  r := ComputeIsGoodParensAux(s, 0);
}
