datatype OptionalString = NoneString | SomeString(value: string)

function LongestSpec(strings: seq<string>): OptionalString
  decreases |strings|
{
  if |strings| == 0 then NoneString
  else
    var tail := LongestSpec(strings[1..]);
    if tail.NoneString? then SomeString(strings[0])
    else if |strings[0]| >= |tail.value| then SomeString(strings[0])
    else tail
}

method longest(strings: seq<string>) returns (result: OptionalString)
  ensures result == LongestSpec(strings)
  decreases |strings|
{
  if |strings| == 0 {
    result := NoneString;
  } else {
    var tail := longest(strings[1..]);
    if tail.NoneString? {
      result := SomeString(strings[0]);
    } else if |strings[0]| >= |tail.value| {
      result := SomeString(strings[0]);
    } else {
      result := tail;
    }
  }
}
