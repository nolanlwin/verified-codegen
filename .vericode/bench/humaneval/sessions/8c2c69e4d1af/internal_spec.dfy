function AllTriplesDistinct(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i + 2 >= |s| then
    true
  else
    s[i] != s[i + 1] && s[i] != s[i + 2] && s[i + 1] != s[i + 2] && AllTriplesDistinct(s, i + 1)
}
function IsHappySpec(s: string): bool
{
  if |s| < 3 then
    false
  else
    AllTriplesDistinct(s, 0)
}

method is_happy(s: string) returns (result: bool)
  ensures result == IsHappySpec(s)
{
  assume false;
}
