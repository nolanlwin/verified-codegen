function PolySpec(xs: seq<real>, x: real): real
  decreases |xs|
{
  if |xs| == 0 then 0.0 else xs[0] + x * PolySpec(xs[1..], x)
}

function FindZeroSpec(xs: seq<real>): real
{
  if exists x: real :: PolySpec(xs, x) == 0.0 then
    var x: real :| PolySpec(xs, x) == 0.0; x
  else
    0.0
}

lemma FindZeroSpecIsRoot(xs: seq<real>)
  requires exists x: real :: PolySpec(xs, x) == 0.0
  ensures PolySpec(xs, FindZeroSpec(xs)) == 0.0
{
}

ghost method FindZero(xs: seq<real>) returns (r: real)
  requires |xs| > 0
  requires |xs| % 2 == 0
  requires xs[|xs| - 1] != 0.0
  requires exists x: real :: PolySpec(xs, x) == 0.0
  ensures r == FindZeroSpec(xs)
  ensures PolySpec(xs, r) == 0.0
{
  r := FindZeroSpec(xs);
  FindZeroSpecIsRoot(xs);
}
