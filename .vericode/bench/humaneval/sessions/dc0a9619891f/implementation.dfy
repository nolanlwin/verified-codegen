function NoDivisorFrom(n: int, d: int): bool
  decreases if n - d < 0 then 0 else n - d
{
  if d >= n then true else n % d != 0 && NoDivisorFrom(n, d + 1)
}

function IsPrimeSpec(n: int): bool
{
  n > 1 && NoDivisorFrom(n, 2)
}

function ExistsPrimeFactorZ(a: int, x: int, y: int, z: int): bool
  decreases 100 - z
{
  if z == 100 then false
  else (IsPrimeSpec(x) && IsPrimeSpec(y) && IsPrimeSpec(z) && x * y * z == a) || ExistsPrimeFactorZ(a, x, y, z + 1)
}

function ExistsPrimeFactorY(a: int, x: int, y: int): bool
  decreases 100 - y
{
  if y == 100 then false
  else ExistsPrimeFactorZ(a, x, y, 2) || ExistsPrimeFactorY(a, x, y + 1)
}

function ExistsPrimeFactorX(a: int, x: int): bool
  decreases 100 - x
{
  if x == 100 then false
  else ExistsPrimeFactorY(a, x, 2) || ExistsPrimeFactorX(a, x + 1)
}

function IsMultiplyPrimeSpec(a: int): bool
{
  ExistsPrimeFactorX(a, 2)
}

method is_multiply_prime(a: int) returns (result: bool)
  requires a < 100
  ensures result == IsMultiplyPrimeSpec(a)
{
  var r := CheckExistsPrimeFactorX(a, 2);
  result := r;
  assert IsMultiplyPrimeSpec(a) == ExistsPrimeFactorX(a, 2);
}

method CheckNoDivisorFrom(n: int, d: int) returns (r: bool)
  requires d > 0
  decreases if n - d < 0 then 0 else n - d
  ensures r == NoDivisorFrom(n, d)
{
  if d >= n {
    r := true;
    assert NoDivisorFrom(n, d) == true;
  } else {
    assert d != 0;
    var sub := CheckNoDivisorFrom(n, d + 1);
    r := n % d != 0 && sub;
    assert NoDivisorFrom(n, d) == (n % d != 0 && NoDivisorFrom(n, d + 1));
  }
}

method CheckIsPrime(n: int) returns (r: bool)
  ensures r == IsPrimeSpec(n)
{
  if n > 1 {
    var nd := CheckNoDivisorFrom(n, 2);
    r := nd;
    assert IsPrimeSpec(n) == NoDivisorFrom(n, 2);
  } else {
    r := false;
    assert IsPrimeSpec(n) == false;
  }
}

method CheckExistsPrimeFactorZ(a: int, x: int, y: int, z: int) returns (r: bool)
  requires z <= 100
  decreases 100 - z
  ensures r == ExistsPrimeFactorZ(a, x, y, z)
{
  if z == 100 {
    r := false;
    assert ExistsPrimeFactorZ(a, x, y, z) == false;
  } else {
    assert z < 100;
    var px := CheckIsPrime(x);
    var py := CheckIsPrime(y);
    var pz := CheckIsPrime(z);
    var hit := px && py && pz && x * y * z == a;
    assert hit == (IsPrimeSpec(x) && IsPrimeSpec(y) && IsPrimeSpec(z) && x * y * z == a);
    assert ExistsPrimeFactorZ(a, x, y, z) == ((IsPrimeSpec(x) && IsPrimeSpec(y) && IsPrimeSpec(z) && x * y * z == a) || ExistsPrimeFactorZ(a, x, y, z + 1));
    if hit {
      r := true;
      assert IsPrimeSpec(x) && IsPrimeSpec(y) && IsPrimeSpec(z) && x * y * z == a;
      assert ExistsPrimeFactorZ(a, x, y, z);
    } else {
      var rest := CheckExistsPrimeFactorZ(a, x, y, z + 1);
      r := rest;
      assert !(IsPrimeSpec(x) && IsPrimeSpec(y) && IsPrimeSpec(z) && x * y * z == a);
      assert ExistsPrimeFactorZ(a, x, y, z) == ExistsPrimeFactorZ(a, x, y, z + 1);
    }
  }
}

method CheckExistsPrimeFactorY(a: int, x: int, y: int) returns (r: bool)
  requires y <= 100
  decreases 100 - y
  ensures r == ExistsPrimeFactorY(a, x, y)
{
  if y == 100 {
    r := false;
    assert ExistsPrimeFactorY(a, x, y) == false;
  } else {
    assert y < 100;
    var first := CheckExistsPrimeFactorZ(a, x, y, 2);
    assert ExistsPrimeFactorY(a, x, y) == (ExistsPrimeFactorZ(a, x, y, 2) || ExistsPrimeFactorY(a, x, y + 1));
    if first {
      r := true;
      assert ExistsPrimeFactorZ(a, x, y, 2);
      assert ExistsPrimeFactorY(a, x, y);
    } else {
      var rest := CheckExistsPrimeFactorY(a, x, y + 1);
      r := rest;
      assert !ExistsPrimeFactorZ(a, x, y, 2);
      assert ExistsPrimeFactorY(a, x, y) == ExistsPrimeFactorY(a, x, y + 1);
    }
  }
}

method CheckExistsPrimeFactorX(a: int, x: int) returns (r: bool)
  requires x <= 100
  decreases 100 - x
  ensures r == ExistsPrimeFactorX(a, x)
{
  if x == 100 {
    r := false;
    assert ExistsPrimeFactorX(a, x) == false;
  } else {
    assert x < 100;
    var first := CheckExistsPrimeFactorY(a, x, 2);
    assert ExistsPrimeFactorX(a, x) == (ExistsPrimeFactorY(a, x, 2) || ExistsPrimeFactorX(a, x + 1));
    if first {
      r := true;
      assert ExistsPrimeFactorY(a, x, 2);
      assert ExistsPrimeFactorX(a, x);
    } else {
      var rest := CheckExistsPrimeFactorX(a, x + 1);
      r := rest;
      assert !ExistsPrimeFactorY(a, x, 2);
      assert ExistsPrimeFactorX(a, x) == ExistsPrimeFactorX(a, x + 1);
    }
  }
}
