function NoDivisorsSpec(n: int, d: int): bool
  decreases n - d
{
  if d == n then true
  else if n % d == 0 then false
  else NoDivisorsSpec(n, d + 1)
}

function IsPrimeSpec(n: int): bool
{
  if n <= 1 then false
  else NoDivisorsSpec(n, 2)
}

function XOrYSpec(n: int, x: int, y: int): int
{
  if IsPrimeSpec(n) then x else y
}

method x_or_y(n: int, x: int, y: int) returns (result: int)
  ensures result == XOrYSpec(n, x, y)
{
  var p := IsPrime(n);
  if p {
    assert IsPrimeSpec(n);
    assert XOrYSpec(n, x, y) == x;
    result := x;
  } else {
    assert !IsPrimeSpec(n);
    assert XOrYSpec(n, x, y) == y;
    result := y;
  }
}

method NoDivisors(n: int, d: int) returns (r: bool)
  requires 2 <= d <= n
  ensures r == NoDivisorsSpec(n, d)
  decreases n - d
{
  if d == n {
    r := true;
  } else if n % d == 0 {
    r := false;
  } else {
    r := NoDivisors(n, d + 1);
    assert NoDivisorsSpec(n, d) == NoDivisorsSpec(n, d + 1);
  }
}

method IsPrime(n: int) returns (r: bool)
  ensures r == IsPrimeSpec(n)
{
  if n <= 1 {
    r := false;
  } else {
    r := NoDivisors(n, 2);
    assert IsPrimeSpec(n) == NoDivisorsSpec(n, 2);
  }
}
