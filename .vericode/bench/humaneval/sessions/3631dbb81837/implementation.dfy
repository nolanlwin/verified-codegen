function AddSpec(x: int, y: int): int
  decreases if y < 0 then -y else y
{
  if y == 0 then x else if y > 0 then AddSpec(x + 1, y - 1) else AddSpec(x - 1, y + 1)
}

method add(x: int, y: int) returns (result: int)
  ensures result == AddSpec(x, y)
  decreases if y < 0 then -y else y
{
  if y == 0 {
    result := x;
  } else if y > 0 {
    result := add(x + 1, y - 1);
  } else {
    result := add(x - 1, y + 1);
  }
}
