function BelowZeroSpec(operations: seq<int>, balance: int): bool
  decreases |operations|
{
  if |operations| == 0 then
    false
  else if balance + operations[0] < 0 then
    true
  else
    BelowZeroSpec(operations[1..], balance + operations[0])
}

method below_zero(operations: seq<int>) returns (result: bool)
  requires true
  ensures result == BelowZeroSpec(operations, 0)
{
  result := BelowZeroHelper(operations, 0);
}

method BelowZeroHelper(operations: seq<int>, balance: int) returns (result: bool)
  ensures result == BelowZeroSpec(operations, balance)
  decreases |operations|
{
  if |operations| == 0 {
    result := false;
  } else if balance + operations[0] < 0 {
    result := true;
  } else {
    result := BelowZeroHelper(operations[1..], balance + operations[0]);
  }
}
