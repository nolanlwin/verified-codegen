function DecodeCyclicSpec(s: string): string
  decreases |s|
{
  if |s| < 3 then s else s[2..3] + s[0..1] + s[1..2] + DecodeCyclicSpec(s[3..])
}

method decode_cyclic(s: string) returns (result: string)
  ensures result == DecodeCyclicSpec(s)
  decreases |s|
{
  if |s| < 3 {
    result := s;
  } else {
    var rest := decode_cyclic(s[3..]);
    result := s[2..3] + s[0..1] + s[1..2] + rest;
  }
}
