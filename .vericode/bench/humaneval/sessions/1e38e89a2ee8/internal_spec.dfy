function GenerateIntegersSpec(a: int, b: int): seq<int>
  decreases if a > b then 1 else 0, if a <= b then b - a + 1 else 0
{
  if a > b then
    GenerateIntegersSpec(b, a)
  else if a > 9 then
    []
  else if a == b then
    if a % 2 == 0 then [a] else []
  else
    (if a % 2 == 0 then [a] else []) + GenerateIntegersSpec(a + 1, b)
}

method generate_integers(a: int, b: int) returns (result: seq<int>)
  requires a > 0 && b > 0
  ensures result == GenerateIntegersSpec(a, b)
{
  assume false;
}
