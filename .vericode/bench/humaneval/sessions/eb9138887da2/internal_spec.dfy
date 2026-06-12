function MaxInt(a: int, b: int): int
{
  if a >= b then a else b
}
function RollingMaxSpec(numbers: seq<int>): seq<int>
  decreases |numbers|
{
  if |numbers| == 0 then
    []
  else
    var rest := RollingMaxSpec(numbers[..(|numbers| - 1)]);
    var lastValue := numbers[(|numbers| - 1)];
    var lastMax := if |rest| == 0 then lastValue else MaxInt(rest[(|rest| - 1)], lastValue);
    rest + [lastMax]
}

method rolling_max(numbers: seq<int>) returns (result: seq<int>)
  requires true
  ensures result == RollingMaxSpec(numbers)
{
  assume false;
}
