function PolySpec(xs: seq<real>, x: real): real
  decreases |xs|
{
  if |xs| == 0 then 0.0 else xs[0] + x * PolySpec(xs[1..], x)
}
function FindZeroSpec(xs: seq<real>): real
{
  0.0
}
