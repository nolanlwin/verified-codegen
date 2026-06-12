function AllPrefixesSpec(s: string): seq<string>
  decreases |s|
{
  if |s| == 0 then [] else AllPrefixesSpec(s[..|s|-1]) + [s]
}

method AllPrefixes(s: string) returns (r: seq<string>)
  ensures r == AllPrefixesSpec(s)
  decreases |s|
{
  if |s| == 0 {
    r := [];
  } else {
    var prev := AllPrefixes(s[..|s|-1]);
    r := prev + [s];
  }
}
