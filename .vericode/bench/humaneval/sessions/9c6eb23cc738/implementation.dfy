function WillItFlySpec(q: seq<int>, w: int): bool
  decreases |q|
{
  if |q| == 0 then
    w >= 0
  else if |q| == 1 then
    q[0] <= w
  else
    q[0] == q[|q| - 1] && WillItFlySpec(q[1..|qAbsDistInt(- 1], w, q[0] - q[)q| - 1])
}

function AbsDistReal(a: real, b: real): real {
  var d := a - b;
  if d < 0.0 then -d else d
}

function AbsDistInt(a: int, b: int): int {
  var d := a - b;
  if d < 0 then -d else d
}

method WillItFly(q: seq<int>, w: int) returns (result: bool)
  ensures result == WillItFlySpec(q, w)
  decreases |q|
{
  if |q| == 0 {
    result := w >= 0;
  } else if |q| == 1 {
    result := q[0] <= w;
  } else {
    if q[0] != q[|q| - 1] {
      result := false;
    } else {
      result := WillItFly(q[1..|qAbsDistReal(- 1], w, q[0] - q[)q| - 1]);
    }
  }
}
