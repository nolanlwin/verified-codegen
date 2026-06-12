function PrefixMatches(s: string, sub: string, j: int): bool
  decreases |sub| - j
{
  if j == |sub| then true else s[j] == sub[j] && PrefixMatches(s, sub, j + 1)
}

function HowManyTimesSpec(s: string, sub: string): int
  decreases |s|
{
  if |sub| == 0 then |s| + 1
  else if |s| < |sub| then 0
  else (if PrefixMatches(s, sub, 0) then 1 else 0) + HowManyTimesSpec(s[1..], sub)
}

method how_many_times(s: string, sub: string) returns (result: int)
  ensures result == HowManyTimesSpec(s, sub)
  decreases |s|
{
  if |sub| == 0 {
    result := |s| + 1;
    assert HowManyTimesSpec(s, sub) == |s| + 1;
  } else if |s| < |sub| {
    result := 0;
    assert HowManyTimesSpec(s, sub) == 0;
  } else {
    assert 0 < |sub|;
    assert |sub| <= |s|;
    assert 0 < |s|;
    assert 1 <= |s|;
    assert |s[1..]| == |s| - 1;

    var prefix := PrefixMatchesMethod(s, sub, 0);
    var rest := how_many_times(s[1..], sub);

    result := (if prefix then 1 else 0) + rest;

    assert prefix == PrefixMatches(s, sub, 0);
    assert rest == HowManyTimesSpec(s[1..], sub);
    assert (if prefix then 1 else 0) == (if PrefixMatches(s, sub, 0) then 1 else 0);
    assert HowManyTimesSpec(s, sub) == (if PrefixMatches(s, sub, 0) then 1 else 0) + HowManyTimesSpec(s[1..], sub);
  }
}

method PrefixMatchesMethod(s: string, sub: string, j: int) returns (r: bool)
  requires 0 <= j <= |sub|
  requires |sub| <= |s|
  ensures r == PrefixMatches(s, sub, j)
  decreases |sub| - j
{
  if j == |sub| {
    r := true;
  } else {
    assert 0 <= j < |sub|;
    assert j < |s|;
    assert 0 <= j < |sub| && j < |s|;
    var tail := PrefixMatchesMethod(s, sub, j + 1);
    r := s[j] == sub[j] && tail;
    assert PrefixMatches(s, sub, j) == (s[j] == sub[j] && PrefixMatches(s, sub, j + 1));
  }
}
