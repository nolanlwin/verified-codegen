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
  decreases |a|
{
  if |a| == 0 {
    result := "";
  } else {
    assert |b| > 0;
    assert |a[1..]| == |b[1..]|;
    assert IsBinaryString(a[1..]);
    assert IsBinaryString(b[1..]);
    var tail := string_xor(a[1..], b[1..]);
    if a[0] == b[0] {
      result := "0" + tail;
    } else {
      result := "1" + tail;
    }
  }
}
