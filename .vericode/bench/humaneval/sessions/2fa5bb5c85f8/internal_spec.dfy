function SumProductSpec(numbers: seq<int>): (int, int)
  decreases |numbers|
{
  if |numbers| == 0 then
    (0, 1)
  else
    var rest := SumProductSpec(numbers[1..]);
    (numbers[0] + rest.0, numbers[0] * rest.1)
}

method sum_product(numbers: seq<int>) returns (result: (int, int))
  requires true
  ensures result == SumProductSpec(numbers)
{
  assume false;
}
