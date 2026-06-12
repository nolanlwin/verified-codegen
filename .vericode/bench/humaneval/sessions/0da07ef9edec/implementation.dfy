function Pow(base: int, exp: int): int
  decreases exp
{
  if exp == 0 then 1 else base * Pow(base, exp - 1)
}

function IsSimplePowerSearch(x: int, n: int, k: int): bool
  decreases k
{
  if Pow(n, k) == x then true
  else if k == 0 then false
  else IsSimplePowerSearch(x, n, k - 1)
}

function IsSimplePowerSpec(x: int, n: int): bool
{
  IsSimplePowerSearch(x, n, if x < 0 then -x + 1 else x + 1)
}

method is_simple_power(x: int, n: int) returns (result: bool)
  ensures result == IsSimplePowerSpec(x, n)
{
  var k := if x < 0 then -x + 1 else x + 1;
  if x < 0 {
    assert -x > 0;
    assert k >= 0;
  } else {
    assert x >= 0;
    assert k >= 0;
  }
  result := IsSimplePowerSearchMethod(x, n, k);
  assert result == IsSimplePowerSearch(x, n, k);
  assert IsSimplePowerSpec(x, n) == IsSimplePowerSearch(x, n, k);
}

method PowMethod(base: int, exp: int) returns (result: int)
  requires exp >= 0
  ensures result == Pow(base, exp)
  decreases exp
{
  if exp == 0 {
    result := 1;
    assert Pow(base, exp) == 1;
  } else {
    assert exp > 0;
    assert exp - 1 >= 0;
    var sub := PowMethod(base, exp - 1);
    result := base * sub;
    assert Pow(base, exp) == base * Pow(base, exp - 1);
  }
}

method IsSimplePowerSearchMethod(x: int, n: int, k: int) returns (result: bool)
  requires k >= 0
  ensures result == IsSimplePowerSearch(x, n, k)
  decreases k
{
  var p := PowMethod(n, k);
  if p == x {
    assert Pow(n, k) == x;
    result := true;
    assert IsSimplePowerSearch(x, n, k) == true;
  } else if k == 0 {
    assert Pow(n, k) != x;
    assert k <= 0;
    result := false;
    assert IsSimplePowerSearch(x, n, k) == false;
  } else {
    assert Pow(n, k) != x;
    assert k != 0;
    assert k > 0;
    assert k - 1 >= 0;
    var r := IsSimplePowerSearchMethod(x, n, k - 1);
    result := r;
    assert !(k <= 0);
    assert IsSimplePowerSearch(x, n, k) == IsSimplePowerSearch(x, n, k - 1);
  }
}
