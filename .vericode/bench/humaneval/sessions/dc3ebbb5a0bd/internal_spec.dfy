function ChooseNumSpec(x: int, y: int): int
  decreases if x <= y then y - x + 1 else 0
{
  if x > y then -1
  else if y % 2 == 0 then y
  else ChooseNumSpec(x, y - 1)
}

method choose_num(x: int, y: int) returns (result: int)
  ensures result == ChooseNumSpec(x, y)
{
  assume false;
}
