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
  result := CorrectBracketingAux(brackets, 0, 0);
}

method CorrectBracketingAux(brackets: string, i: int, balance: int) returns (result: bool)
  requires 0 <= i <= |brackets|
  ensures result == CorrectBracketingSpec(brackets, i, balance)
  decreases |brackets| - i
{
  if i == |brackets| {
    result := balance == 0;
  } else if brackets[i] == "("[0] {
    result := CorrectBracketingAux(brackets, i + 1, balance + 1);
  } else if brackets[i] == ")"[0] {
    if balance > 0 {
      result := CorrectBracketingAux(brackets, i + 1, balance - 1);
    } else {
      result := false;
    }
  } else {
    result := false;
  }
}
