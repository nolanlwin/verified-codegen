function DividesAny(n: int, d: int): bool
  decreases d
{
  if d < 2 then false else if n % d == 0 then true else DividesAny(n, d - 1)
}

function IsPrime(n: int): bool
{
  if n < 2 then false else !DividesAny(n, n - 1)
}

function DigitSum(n: int): int
  decreases n
{
  if n < 10 then n else n % 10 + DigitSum(n / 10)
}

function MaxPrimeAux(lst: seq<int>, i: int, current: int): int
  decreases |lst| - i
{
  if i == |lst| then current
  else if IsPrime(lst[i]) && lst[i] > current then MaxPrimeAux(lst, i + 1, lst[i])
  else MaxPrimeAux(lst, i + 1, current)
}

function SkjkasdkdSpec(lst: seq<int>): int
  decreases |lst|
{
  var m := MaxPrimeAux(lst, 0, -1);
  if |lst| == 0 then 0 else if m < 0 then SkjkasdkdSpec(lst[1..]) else DigitSum(m)
}

method skjkasdkd(lst: seq<int>) returns (result: int)
  requires true
  ensures result == SkjkasdkdSpec(lst)
  decreases |lst|
{
  if |lst| == 0 {
    result := 0;
  } else {
    assert 0 < |lst|;
    var m := MaxPrimeAuxM(lst, 0, -1);
    assert m == MaxPrimeAux(lst, 0, -1);
    if m < 0 {
      assert |lst[1..]| == |lst| - 1;
      result := skjkasdkd(lst[1..]);
      assert result == SkjkasdkdSpec(lst[1..]);
      assert SkjkasdkdSpec(lst) == SkjkasdkdSpec(lst[1..]);
    } else {
      result := DigitSumM(m);
      assert result == DigitSum(m);
      assert SkjkasdkdSpec(lst) == DigitSum(m);
    }
  }
}

method DividesAnyM(n: int, d: int) returns (b: bool)
  ensures b == DividesAny(n, d)
  decreases d
{
  if d < 2 {
    b := false;
  } else if n % d == 0 {
    b := true;
  } else {
    b := DividesAnyM(n, d - 1);
  }
}

method IsPrimeM(n: int) returns (b: bool)
  ensures b == IsPrime(n)
{
  if n < 2 {
    b := false;
  } else {
    var hasDivisor := DividesAnyM(n, n - 1);
    b := !hasDivisor;
  }
}

method DigitSumM(n: int) returns (s: int)
  ensures s == DigitSum(n)
  decreases n
{
  if n < 10 {
    s := n;
  } else {
    assert 0 <= n / 10;
    assert n / 10 < n;
    var rest := DigitSumM(n / 10);
    s := n % 10 + rest;
  }
}

method MaxPrimeAuxM(lst: seq<int>, i: int, current: int) returns (res: int)
  requires 0 <= i <= |lst|
  ensures res == MaxPrimeAux(lst, i, current)
  decreases |lst| - i
{
  if i == |lst| {
    res := current;
  } else {
    assert 0 <= i < |lst|;
    var p := IsPrimeM(lst[i]);
    if p && lst[i] > current {
      assert IsPrime(lst[i]) && lst[i] > current;
      res := MaxPrimeAuxM(lst, i + 1, lst[i]);
    } else {
      assert !(p && lst[i] > current);
      assert !(IsPrime(lst[i]) && lst[i] > current);
      res := MaxPrimeAuxM(lst, i + 1, current);
    }
  }
}
