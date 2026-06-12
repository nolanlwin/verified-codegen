datatype PyValue = PyInt(i: int) | PyOther

function FilterIntegersSpec(values: seq<PyValue>): seq<int>
  decreases |values|
{
  if |values| == 0 then
    []
  else if values[0].PyInt? then
    [values[0].i] + FilterIntegersSpec(values[1..])
  else
    FilterIntegersSpec(values[1..])
}

method filter_integers(values: seq<PyValue>) returns (result: seq<int>)
  ensures result == FilterIntegersSpec(values)
  decreases |values|
{
  if |values| == 0 {
    result := [];
  } else {
    var tail := filter_integers(values[1..]);
    if values[0].PyInt? {
      result := [values[0].i] + tail;
    } else {
      result := tail;
    }
  }
}
