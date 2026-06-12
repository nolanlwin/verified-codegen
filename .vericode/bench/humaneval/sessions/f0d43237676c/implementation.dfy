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
  var name := StrongestExtensionName(extensions);
  result := class_name + "." + name;
}

method ExtensionStrength(extension: string) returns (strength: int)
  ensures strength == ExtensionStrengthSpec(extension)
  decreases |extension|
{
  if |extension| == 0 {
    strength := 0;
  } else {
    var tailStrength := ExtensionStrength(extension[1..]);
    var contribution := if IsUppercaseLetter(extension[0]) then 1
                        else if IsLowercaseLetter(extension[0]) then -1
                        else 0;
    strength := contribution + tailStrength;
  }
}

method StrongestExtensionName(extensions: seq<string>) returns (name: string)
  requires |extensions| > 0
  ensures name == StrongestExtensionNameSpec(extensions)
  decreases |extensions|
{
  if |extensions| == 1 {
    name := extensions[0];
  } else {
    assert |extensions| > 1;
    assert |extensions[1..]| > 0;
    var tailBest := StrongestExtensionName(extensions[1..]);
    var headStrength := ExtensionStrength(extensions[0]);
    var tailStrength := ExtensionStrength(tailBest);

    assert tailBest == StrongestExtensionNameSpec(extensions[1..]);
    assert headStrength == ExtensionStrengthSpec(extensions[0]);
    assert tailStrength == ExtensionStrengthSpec(tailBest);
    assert StrongestExtensionNameSpec(extensions) ==
      (if ExtensionStrengthSpec(extensions[0]) >= ExtensionStrengthSpec(tailBest) then extensions[0] else tailBest);

    if headStrength >= tailStrength {
      assert ExtensionStrengthSpec(extensions[0]) >= ExtensionStrengthSpec(tailBest);
      name := extensions[0];
    } else {
      assert ExtensionStrengthSpec(extensions[0]) < ExtensionStrengthSpec(tailBest);
      name := tailBest;
    }
  }
}
