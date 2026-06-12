function IsUppercaseLetter(c: char): bool
{
  'A' <= c && c <= 'Z'
}
function IsLowercaseLetter(c: char): bool
{
  'a' <= c && c <= 'z'
}
function ExtensionStrengthSpec(extension: string): int
  decreases |extension|
{
  if |extension| == 0 then 0
  else
    (if IsUppercaseLetter(extension[0]) then 1
     else if IsLowercaseLetter(extension[0]) then -1
     else 0) + ExtensionStrengthSpec(extension[1..])
}
function StrongestExtensionNameSpec(extensions: seq<string>): string
  decreases |extensions|
{
  if |extensions| == 1 then extensions[0]
  else
    var tailBest := StrongestExtensionNameSpec(extensions[1..]);
    if ExtensionStrengthSpec(extensions[0]) >= ExtensionStrengthSpec(tailBest) then extensions[0] else tailBest
}
function StrongestExtensionSpec(class_name: string, extensions: seq<string>): string
{
  class_name + "." + StrongestExtensionNameSpec(extensions)
}

method Strongest_Extension(class_name: string, extensions: seq<string>) returns (result: string)
  requires |extensions| > 0
  ensures result == StrongestExtensionSpec(class_name, extensions)
{
  assume false;
}
