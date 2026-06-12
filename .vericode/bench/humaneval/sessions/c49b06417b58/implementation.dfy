function TriangleAreaHalf(x: real, n: int): real
  decreases n
{
  if n == 1 then x else TriangleAreaHalf(x / 2.0, n - 1)
}

function TriangleAreaSpec(a: real, h: real): real
{
  TriangleAreaHalf(a * h, 2)
}

method triangle_area(a: real, h: real) returns (result: real)
  ensures result == TriangleAreaSpec(a, h)
{
  result := TriangleAreaSpec(a, h);
}
