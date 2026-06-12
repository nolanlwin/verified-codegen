function DoubleTheDifferenceSpec(lst: seq<int>): int
  decreases |lst|
{
  if |lst| == 0 then 0
  else if lst[0] >= 0 && lst[0] % 2 != 0 then lst[0] * lst[0] + DoubleTheDifferenceSpec(lst[1..])
  else DoubleTheDifferenceSpec(lst[1..])
}

method double_the_difference(lst: seq<int>) returns (result: int)
  ensures result == DoubleTheDifferenceSpec(lst)
  decreases |lst|
{
  if |lst| == 0 {
    result := 0;
  } else {
    var tailResult := double_the_difference(lst[1..]);
    if lst[0] >= 0 && lst[0] % 2 != 0 {
      result := lst[0] * lst[0] + tailResult;
    } else {
      result := tailResult;
    }
  }
}
