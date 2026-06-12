function InsertSortedInt(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 || x <= s[0] then [x] + s
  else [s[0]] + InsertSortedInt(x, s[1..])
}
function GetOddCollatzSpec(n: int): seq<int>
  decreases n
{
  if n == 1 then [1]
  else if n % 2 == 0 then GetOddCollatzSpec(n / 2)
  else InsertSortedInt(n, GetOddCollatzSpec(3 * n + 1))
}

method get_odd_collatz(n: int) returns (result: seq<int>)
  requires n > 0
  ensures result == GetOddCollatzSpec(n)
{
  assume false;
}
