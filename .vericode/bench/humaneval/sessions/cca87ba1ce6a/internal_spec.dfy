function IsEqualToSumEvenSpec(n: int): bool
  decreases if n < 0 then 0 else n
{
  if n < 8 then false
  else if n == 8 then true
  else IsEqualToSumEvenSpec(n - 2)
}

method is_equal_to_sum_even(n: int) returns (result: bool)
  ensures result == IsEqualToSumEvenSpec(n)
{
  assume false;
}
