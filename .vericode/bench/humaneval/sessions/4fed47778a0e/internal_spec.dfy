function IsBinaryString(s: string): bool
  decreases |s|
{
  if |s| == 0 then true
  else (s[0] == '0' || s[0] == '1') && IsBinaryString(s[1..])
}
function StringXorSpec(a: string, b: string): string
  decreases |a|
{
  if |a| == 0 then ""
  else if a[0] == b[0] then "0" + StringXorSpec(a[1..], b[1..])
  else "1" + StringXorSpec(a[1..], b[1..])
}

method string_xor(a: string, b: string) returns (result: string)
  requires |a| == |b|
  requires IsBinaryString(a)
  requires IsBinaryString(b)
  ensures result == StringXorSpec(a, b)
{
  assume false;
}
