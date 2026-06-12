function ConcatenateSpec(strings: seq<string>): string
  decreases |strings|
{
  if |strings| == 0 then "" else strings[0] + ConcatenateSpec(strings[1..])
}

method concatenate(strings: seq<string>) returns (result: string)
  requires true
  ensures result == ConcatenateSpec(strings)
  decreases |strings|
{
  if |strings| == 0 {
    result := "";
  } else {
    var rest := concatenate(strings[1..]);
    result := strings[0] + rest;
  }
}
