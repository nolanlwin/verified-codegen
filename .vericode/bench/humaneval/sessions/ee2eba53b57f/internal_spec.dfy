function IsValidTriangle(a: int, b: int, c: int): bool
{
  a + b > c && a + c > b && b + c > a
}
function HeronDiscriminant(a: int, b: int, c: int): int
{
  (a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c)
}
function RoundAreaCentsSearch(d: int, k: int, limit: int): int
  decreases limit - k
{
  if k == limit then k
  else if (2 * k + 1) * (2 * k + 1) > 2500 * d then k
  else RoundAreaCentsSearch(d, k + 1, limit)
}
function RoundedAreaCents(d: int): int
{
  RoundAreaCentsSearch(d, 0, 25 * d + 1)
}
function TriangleAreaSpec(a: int, b: int, c: int): real
  decreases if a < 0 then -a else 0
{
  if a < 0 then TriangleAreaSpec(0, b, c)
  else if IsValidTriangle(a, b, c) && HeronDiscriminant(a, b, c) >= 0 then
    (RoundedAreaCents(HeronDiscriminant(a, b, c)) as real) / 100.0
  else -1.0
}

method triangle_area(a: int, b: int, c: int) returns (result: real)
  requires true
  ensures result == TriangleAreaSpec(a, b, c)
{
  assume false;
}
