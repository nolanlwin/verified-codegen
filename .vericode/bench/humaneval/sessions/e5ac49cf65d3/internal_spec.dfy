function OrderedValuePair(x: real, y: real): (real, real)
{
  if x <= y then (x, y) else (y, x)
}
function AbsReal(x: real): real
{
  if x < 0.0 then -x else x
}
function PairGap(p: (real, real)): real
{
  AbsReal(p.1 - p.0)
}
function BetterPair(p: (real, real), q: (real, real)): (real, real)
{
  if PairGap(p) <= PairGap(q) then p else q
}
function ClosestToValueSpec(x: real, numbers: seq<real>): (real, real)
  decreases |numbers|
{
  if |numbers| == 1 then OrderedValuePair(x, numbers[0])
  else BetterPair(OrderedValuePair(x, numbers[0]), ClosestToValueSpec(x, numbers[1..]))
}
function FindClosestElementsSpec(numbers: seq<real>): (real, real)
  decreases |numbers|
{
  0
}
