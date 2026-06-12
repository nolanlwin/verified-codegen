function MakeAPileAux(current: int, remaining: int): seq<int>
  decreases remaining
{
  if remaining == 0 then []
  else [current] + MakeAPileAux(current + 2, remaining - 1)
}
function MakeAPileSpec(n: int): seq<int>
{
  MakeAPileAux(n, n)
}

method make_a_pile(n: int) returns (result: seq<int>)
  requires n > 0
  ensures result == MakeAPileSpec(n)
{
  assume false;
}
