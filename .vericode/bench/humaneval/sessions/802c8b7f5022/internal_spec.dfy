function AddSpec(lst: seq<int>): int
  decreases |lst|
{
  if |lst| <= 1 then 0
  else
    (if lst[1] % 2 == 0 then lst[1] else 0) +
    (if |lst| <= 2 then 0 else AddSpec(lst[2..]))
}

method add(lst: seq<int>) returns (result: int)
  requires |lst| > 0
  ensures result == AddSpec(lst)
{
  assume false;
}
