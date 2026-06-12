function EatSpec(number: int, need: int, remaining: int): seq<int>
  decreases need
{
  if need == 0 || remaining == 0 then [number, remaining] else EatSpec(number + 1, need - 1, remaining - 1)
}

method eat(number: int, need: int, remaining: int) returns (result: seq<int>)
  requires 0 <= number <= 1000
  requires 0 <= need <= 1000
  requires 0 <= remaining <= 1000
  ensures result == EatSpec(number, need, remaining)
{
  assume false;
}
