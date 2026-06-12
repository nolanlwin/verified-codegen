function ContainsChar(s: string, c: char, i: int): bool
  decreases |s| - i
{
  if i == |s| then false else s[i] == c || ContainsChar(s, c, i + 1)
}

function AllCharsIn(s0: string, s1: string, i: int): bool
  decreases |s0| - i
{
  if i == |s0| then true else ContainsChar(s1, s0[i], 0) && AllCharsIn(s0, s1, i + 1)
}

function SameCharsSpec(s0: string, s1: string): bool
{
  AllCharsIn(s0, s1, 0) && AllCharsIn(s1, s0, 0)
}

method same_chars(s0: string, s1: string) returns (result: bool)
  ensures result == SameCharsSpec(s0, s1)
{
  var left := AllCharsInMethod(s0, s1, 0);
  var right := AllCharsInMethod(s1, s0, 0);
  result := left && right;
}

method ContainsCharMethod(s: string, c: char, i: int) returns (result: bool)
  requires 0 <= i <= |s|
  ensures result == ContainsChar(s, c, i)
  decreases |s| - i
{
  if i == |s| {
    result := false;
  } else {
    assert 0 <= i < |s|;
    var rest := ContainsCharMethod(s, c, i + 1);
    result := s[i] == c || rest;
  }
}

method AllCharsInMethod(s0: string, s1: string, i: int) returns (result: bool)
  requires 0 <= i <= |s0|
  ensures result == AllCharsIn(s0, s1, i)
  decreases |s0| - i
{
  if i == |s0| {
    result := true;
  } else {
    assert 0 <= i < |s0|;
    var has := ContainsCharMethod(s1, s0[i], 0);
    var rest := AllCharsInMethod(s0, s1, i + 1);
    result := has && rest;
  }
}
