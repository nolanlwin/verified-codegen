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
  decreases *
{
  if n == 1 {
    result := [1];
    GetOddCollatzSpecOne();
    assert GetOddCollatzSpec(n) == [1];
  } else if n % 2 == 0 {
    assert n != 0;
    assert n == (n / 2) * 2 + n % 2;
    assert n == (n / 2) * 2;
    assert n / 2 >= 0;
    assert n / 2 != 0;
    assert n / 2 > 0;
    result := get_odd_collatz(n / 2);
    assert result == GetOddCollatzSpec(n / 2);
    GetOddCollatzSpecEven(n);
    assert GetOddCollatzSpec(n) == GetOddCollatzSpec(n / 2);
  } else {
    assert n > 1;
    assert 3 * n + 1 > 0;
    var tail := get_odd_collatz(3 * n + 1);
    assert tail == GetOddCollatzSpec(3 * n + 1);
    result := InsertSortedInt(n, tail);
    assert result == InsertSortedInt(n, GetOddCollatzSpec(3 * n + 1));
    GetOddCollatzSpecOdd(n);
    assert GetOddCollatzSpec(n) == InsertSortedInt(n, GetOddCollatzSpec(3 * n + 1));
  }
}
