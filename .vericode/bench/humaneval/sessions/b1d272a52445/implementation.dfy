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
  result := MakeAPile(n, n);
}
method MakeAPile(start: int, count: int) returns (result: seq<int>)
  requires count >= 0
  ensures result == MakeAPileAux(start, count)
  decreases count
{
  if count == 0 {
    result := [];
  } else {
    var tail := MakeAPile(start + 2, count - 1);
    result := [start] + tail;
  }
}
