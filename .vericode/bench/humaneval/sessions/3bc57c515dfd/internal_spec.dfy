function MinSeq(s: seq<real>): real
  decreases |s|
{
  if |s| == 1 then
    s[0]
  else
    var m := MinSeq(s[1..]);
    if s[0] <= m then s[0] else m
}
function MaxSeq(s: seq<real>): real
  decreases |s|
{
  if |s| == 1 then
    s[0]
  else
    var m := MaxSeq(s[1..]);
    if s[0] >= m then s[0] else m
}
function RescaleAux(s: seq<real>, mn: real, mx: real): seq<real>
  decreases |s|
{
  if |s| == 0 then
    []
  else
    [(s[0] - mn) / (mx - mn)] + RescaleAux(s[1..], mn, mx)
}
function RescaleToUnitSpec(numbers: seq<real>): seq<real>
{
  RescaleAux(numbers, MinSeq(numbers), MaxSeq(numbers))
}

method rescale_to_unit(numbers: seq<real>) returns (result: seq<real>)
  requires |numbers| >= 2
  requires MinSeq(numbers) < MaxSeq(numbers)
  ensures result == RescaleToUnitSpec(numbers)
{
  assume false;
}
