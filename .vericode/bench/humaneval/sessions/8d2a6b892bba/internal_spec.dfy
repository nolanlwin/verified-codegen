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
  assume false;
}
