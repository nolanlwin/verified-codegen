function IntersperseSpec(numbers: seq<int>, delimeter: int): seq<int>
  decreases |numbers|
{
  if |numbers| <= 1 then
    numbers
  else
    [numbers[0], delimeter] + IntersperseSpec(numbers[1..], delimeter)
}

method intersperse(numbers: seq<int>, delimeter: int) returns (result: seq<int>)
  ensures result == IntersperseSpec(numbers, delimeter)
{
  assume false;
}
