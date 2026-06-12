function AllPositiveSpec(s: seq<int>, i: int): bool
  decreases |s| - i
{
  if i == |s| then true else 0 < s[i] && AllPositiveSpec(s, i + 1)
}

function TriangleInequalitySpec(a: int, b: int, c: int): bool
{
  a + b > c && a + c > b && b + c > a
}

function PythagoreanAtSpec(s: seq<int>, i: int): bool
{
  if i == 0 then s[0] * s[0] == s[1] * s[1] + s[2] * s[2]
  else if i == 1 then s[1] * s[1] == s[0] * s[0] + s[2] * s[2]
  else s[2] * s[2] == s[0] * s[0] + s[1] * s[1]
}

function ExistsPythagoreanHypotenuseSpec(s: seq<int>, i: int): bool
  decreases 3 - i
{
  if i == 3 then false else PythagoreanAtSpec(s, i) || ExistsPythagoreanHypotenuseSpec(s, i + 1)
}

function RightAngleTriangleSpec(a: int, b: int, c: int): bool
{
  var sides := [a, b, c];
  AllPositiveSpec(sides, 0) && TriangleInequalitySpec(a, b, c) && ExistsPythagoreanHypotenuseSpec(sides, 0)
}

method right_angle_triangle(a: int, b: int, c: int) returns (result: bool)
  requires true
  ensures result == RightAngleTriangleSpec(a, b, c)
{
  result := RightAngleTriangleSpec(a, b, c);
}
