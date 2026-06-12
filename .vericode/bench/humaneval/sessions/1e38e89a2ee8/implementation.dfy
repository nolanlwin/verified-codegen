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
  decreases if a > b then 1 else 0, if a <= b then b - a + 1 else 0
{
  if a > b {
    result := generate_integers(b, a);
  } else if a > 9 {
    result := [];
  } else if a == b {
    if a % 2 == 0 {
      result := [a];
    } else {
      result := [];
    }
  } else {
    var tail := generate_integers(a + 1, b);
    if a % 2 == 0 {
      result := [a] + tail;
    } else {
      result := tail;
    }
  }
}
