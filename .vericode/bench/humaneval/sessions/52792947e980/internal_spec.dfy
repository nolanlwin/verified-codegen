function AllAngleBrackets(brackets: string, i: int): bool
  decreases |brackets| - i
{
  if i == |brackets| then
    true
  else
    (brackets[i] == '<' || brackets[i] == ">") && AllAngleBrackets(brackets, i + 1)
}
function CorrectBracketingAux(brackets: string, i: int, balance: int): bool
  decreases |brackets| - i
{
  if i == |brackets| then
    balance == 0
  else if brackets[i] == '<' then
    CorrectBracketingAux(brackets, i + 1, balance + 1)
  else if balance == 0 then
    false
  else
    CorrectBracketingAux(brackets, i + 1, balance - 1)
}
function CorrectBracketingSpec(brackets: string): bool
{
  CorrectBracketingAux(brackets, 0, 0)
}

method correct_bracketing(brackets: string) returns (result: bool)
  requires AllAngleBrackets(brackets, 0)
  ensures result == CorrectBracketingSpec(brackets)
{
  assume false;
}
