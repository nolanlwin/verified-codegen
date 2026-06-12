function Fib4Spec(n: int): int
  decreases n
{
  if n == 0 then 0
  else if n == 1 then 0
  else if n == 2 then 2
  else if n == 3 then 0
  else Fib4Spec(n - 1) + Fib4Spec(n - 2) + Fib4Spec(n - 3) + Fib4Spec(n - 4)
}

method fib4(n: int) returns (result: int)
  requires n >= 0
  ensures result == Fib4Spec(n)
{
  if n == 0 {
    result := 0;
    assert result == Fib4Spec(n);
    return;
  } else if n == 1 {
    result := 0;
    assert result == Fib4Spec(n);
    return;
  } else if n == 2 {
    result := 2;
    assert result == Fib4Spec(n);
    return;
  } else if n == 3 {
    result := 0;
    assert result == Fib4Spec(n);
    return;
  }

  assert n >= 4;

  var i := 3;
  var a := 0;
  var b := 0;
  var c := 2;
  var d := 0;

  assert a == Fib4Spec(i - 3);
  assert b == Fib4Spec(i - 2);
  assert c == Fib4Spec(i - 1);
  assert d == Fib4Spec(i);

  while i < n
    invariant 3 <= i <= n
    invariant a == Fib4Spec(i - 3)
    invariant b == Fib4Spec(i - 2)
    invariant c == Fib4Spec(i - 1)
    invariant d == Fib4Spec(i)
    decreases n - i
  {
    var oldI := i;
    ghost var oldA := a;
    ghost var oldB := b;
    ghost var oldC := c;
    ghost var oldD := d;

    assert oldI >= 3;
    assert oldI - 3 >= 0;
    assert oldI - 2 >= 0;
    assert oldI - 1 >= 0;
    assert oldI >= 0;
    assert oldI + 1 >= 0;
    assert oldA == Fib4Spec(oldI - 3);
    assert oldB == Fib4Spec(oldI - 2);
    assert oldC == Fib4Spec(oldI - 1);
    assert oldD == Fib4Spec(oldI);

    var next := d + c + b + a;

    assert oldI + 1 >= 4;
    assert oldI + 1 != 0;
    assert oldI + 1 != 1;
    assert oldI + 1 != 2;
    assert oldI + 1 != 3;
    assert Fib4Spec(oldI + 1) == Fib4Spec(oldI) + Fib4Spec(oldI - 1) + Fib4Spec(oldI - 2) + Fib4Spec(oldI - 3);
    assert next == Fib4Spec(oldI + 1);

    a, b, c, d := b, c, d, next;
    i := oldI + 1;

    assert a == oldB;
    assert b == oldC;
    assert c == oldD;
    assert d == Fib4Spec(oldI + 1);

    assert i - 3 == oldI - 2;
    assert i - 2 == oldI - 1;
    assert i - 1 == oldI;
    assert i == oldI + 1;

    assert a == Fib4Spec(i - 3);
    assert b == Fib4Spec(i - 2);
    assert c == Fib4Spec(i - 1);
    assert d == Fib4Spec(i);
  }

  assert i == n;
  result := d;
  assert result == Fib4Spec(n);
}
