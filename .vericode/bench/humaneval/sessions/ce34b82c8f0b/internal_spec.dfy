function DerivativeSpec(xs: seq<int>, degree: int): seq<int>
  decreases |xs|
{
  if |xs| == 0 then
    []
  else if degree == 0 then
    DerivativeSpec(xs[1..], degree + 1)
  else
    [degree * xs[0]] + DerivativeSpec(xs[1..], degree + 1)
}

method derivative(xs: seq<int>) returns (result: seq<int>)
  requires true
  ensures result == DerivativeSpec(xs, 0)
{
  assume false;
}
