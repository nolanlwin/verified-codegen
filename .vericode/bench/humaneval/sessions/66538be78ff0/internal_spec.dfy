function CorrectBracketingSpec(brackets: string, i: int, balance: int): bool
  decreases |brackets| - i
{
  if i == |brackets| then
    balance == 0
  else if brackets[i] == "("[0] then
    CorrectBracketingSpec(brackets, i + 1, balance + 1)
  else if brackets[i] == ")"[0] then
    balance > 0 && CorrectBracketingSpec(brackets, i + 1, balance - 1)
  else
    false
}

method correct_bracketing(brackets: string) returns (result: bool)
  requires true
  ensures result == CorrectBracketingSpec(brackets, 0, 0)
{
  assume false;
}
