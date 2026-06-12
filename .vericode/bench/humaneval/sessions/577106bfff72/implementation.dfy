function ContainsFromSpec(a: string, pattern: string, i: int): bool
  decreases |a| - i
{
  if |pattern| == 0 then true
  else if i + |pattern| > |a| then false
  else if a[i..i + |pattern|] == pattern then true
  else ContainsFromSpec(a, pattern, i + 1)
}

function ContainsSpec(a: string, pattern: string): bool
{
  ContainsFromSpec(a, pattern, 0)
}

function RotationContainsFromSpec(a: string, b: string, k: int): bool
  decreases |b| - k
{
  if k == |b| then false
  else if ContainsSpec(a, b[k..] + b[..k]) then true
  else RotationContainsFromSpec(a, b, k + 1)
}

function CycpatternCheckSpec(a: string, b: string): bool
{
  if |b| == 0 then true
  else RotationContainsFromSpec(a, b, 0)
}

method cycpattern_check(a: string, b: string) returns (result: bool)
  ensures result == CycpatternCheckSpec(a, b)
{
  if |b| == 0 {
    result := true;
  } else {
    var r := RotationContainsFrom(a, b, 0);
    result := r;
  }
}

method ContainsFrom(a: string, pattern: string, i: int) returns (result: bool)
  requires 0 <= i
  ensures result == ContainsFromSpec(a, pattern, i)
  decreases |a| - i
{
  if |pattern| == 0 {
    result := true;
  } else if i + |pattern| > |a| {
    result := false;
  } else if a[i..i + |pattern|] == pattern {
    result := true;
  } else {
    assert 0 < |pattern|;
    assert i + |pattern| <= |a|;
    assert i < |a|;
    var r := ContainsFrom(a, pattern, i + 1);
    result := r;
  }
}

method Contains(a: string, pattern: string) returns (result: bool)
  ensures result == ContainsSpec(a, pattern)
{
  var r := ContainsFrom(a, pattern, 0);
  result := r;
}

method RotationContainsFrom(a: string, b: string, k: int) returns (result: bool)
  requires 0 <= k <= |b|
  ensures result == RotationContainsFromSpec(a, b, k)
  decreases |b| - k
{
  if k == |b| {
    result := false;
  } else {
    var rotated := b[k..] + b[..k];
    var c := Contains(a, rotated);
    if c {
      result := true;
    } else {
      assert !ContainsSpec(a, rotated);
      assert k < |b|;
      assert 0 <= k + 1 <= |b|;
      var r := RotationContainsFrom(a, b, k + 1);
      result := r;
    }
  }
}
