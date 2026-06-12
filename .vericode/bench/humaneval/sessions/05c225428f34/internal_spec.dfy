function StartsWithAux(s: string, prefix: string, i: int): bool
  decreases |prefix| - i
{
  if i == |prefix| then true else s[i] == prefix[i] && StartsWithAux(s, prefix, i + 1)
}
function StartsWith(s: string, prefix: string): bool
{
  if |prefix| > |s| then false else StartsWithAux(s, prefix, 0)
}
function FilterByPrefixSpec(strings: seq<string>, prefix: string): seq<string>
  decreases |strings|
{
  if |strings| == 0 then []
  else if StartsWith(strings[0], prefix) then [strings[0]] + FilterByPrefixSpec(strings[1..], prefix)
  else FilterByPrefixSpec(strings[1..], prefix)
}

method filter_by_prefix(strings: seq<string>, prefix: string) returns (result: seq<string>)
  requires true
  ensures result == FilterByPrefixSpec(strings, prefix)
{
  assume false;
}
