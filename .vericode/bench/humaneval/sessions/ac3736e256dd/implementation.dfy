function StrlenSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then 0 else 1 + StrlenSpec(s[1..])
}

method strlen(s: string) returns (result: int)
  requires true
  ensures result == StrlenSpec(s)
  decreases |s|
{
  if |s| == 0 {
    result := 0;
  } else {
    assert 0 < |s|;
    assert |s[1..]| == |s| - 1;
    var tailResult := strlen(s[1..]);
    result := 1 + tailResult;
  }
}
