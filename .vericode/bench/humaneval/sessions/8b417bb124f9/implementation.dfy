function IsValidOperator(op: string): bool
{
  op == "+" || op == "-" || op == "*" || op == "//" || op == "**"
}

function ValidOperators(operators: seq<string>): bool
  decreases |operators|
{
  if |operators| == 0 then true
  else IsValidOperator(operators[0]) && ValidOperators(operators[1..])
}

function NonNegativeOperands(operands: seq<int>): bool
  decreases |operands|
{
  if |operands| == 0 then true
  else operands[0] >= 0 && NonNegativeOperands(operands[1..])
}

function NoImmediateZeroDivisors(operators: seq<string>, operands: seq<int>): bool
  decreases |operators|
{
  if |operators| == 0 then true
  else (operators[0] != "//" || operands[1] != 0) && NoImmediateZeroDivisors(operators[1..], operands[1..])
}

function Pow(base: int, exponent: int): int
  decreases exponent
{
  if exponent == 0 then 1
  else base * Pow(base, exponent - 1)
}

function FindRightmostAddSub(operators: seq<string>): (idx: int)
  ensures -1 <= idx < |operators|
  decreases |operators|
{
  if |operators| == 0 then -1
  else
    var r := FindRightmostAddSub(operators[1..]);
    if r != -1 then r + 1
    else if operators[0] == "+" || operators[0] == "-" then 0
    else -1
}

function FindRightmostMulDiv(operators: seq<string>): (idx: int)
  ensures -1 <= idx < |operators|
  decreases |operators|
{
  if |operators| == 0 then -1
  else
    var r := FindRightmostMulDiv(operators[1..]);
    if r != -1 then r + 1
    else if operators[0] == "*" || operators[0] == "//" then 0
    else -1
}

function FindLeftmostPow(operators: seq<string>): int
  decreases |operators|
{
  if |operators| == 0 then -1
  else if operators[0] == "**" then 0
  else
    var r := FindLeftmostPow(operators[1..]);
    if r == -1 then -1 else r + 1
}

function DoAlgebraSpec(operators: seq<string>, operands: seq<int>): int
  decreases |operators|
{
  if |operators| == 0 then operands[0]
  else
    var add := FindRightmostAddSub(operators);
    if add != -1 then
      if operators[add] == "+" then
        DoAlgebraSpec(operators[..add], operands[..add + 1]) + DoAlgebraSpec(operators[add + 1..], operands[add + 1..])
      else
        DoAlgebraSpec(operators[..add], operands[..add + 1]) - DoAlgebraSpec(operators[add + 1..], operands[add + 1..])
    else
      var mul := FindRightmostMulDiv(operators);
      if mul != -1 then
        if operators[mul] == "*" then
          DoAlgebraSpec(operators[..mul], operands[..mul + 1]) * DoAlgebraSpec(operators[mul + 1..], operands[mul + 1..])
        else
          var divisor := DoAlgebraSpec(operators[mul + 1..], operands[mul + 1..]);
          if divisor == 0 then 0 else DoAlgebraSpec(operators[..mul], operands[..mul + 1]) / divisor
      else
        var pow := FindLeftmostPow(operators);
        if pow != -1 then
          var exponent := DoAlgebraSpec(operators[pow + 1..], operands[pow + 1..]);
          if exponent < 0 then 0 else Pow(DoAlgebraSpec(operators[..pow], operands[..pow + 1]), exponent)
        else operands[0]
}

method do_algebra(operators: seq<string>, operands: seq<int>) returns (result: int)
  requires |operators| + 1 == |operands|
  requires |operators| >= 1
  requires ValidOperators(operators)
  requires NonNegativeOperands(operands)
  requires NoImmediateZeroDivisors(operators, operands)
  ensures result == DoAlgebraSpec(operators, operands)
{
  result := DoAlgebraSpec(operators, operands);
}
