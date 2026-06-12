function SpaceRunSpec(count: nat): string
{
  if count == 0 then ""
  else if count == 1 then "_"
  else if count == 2 then "__"
  else "-"
}

function FixSpacesSpec(text: string, pendingSpaces: nat): string
  decreases |text|
{
  if |text| == 0 then SpaceRunSpec(pendingSpaces)
  else if text[0] == ' ' then FixSpacesSpec(text[1..], pendingSpaces + 1)
  else SpaceRunSpec(pendingSpaces) + text[0..1] + FixSpacesSpec(text[1..], 0)
}

method fix_spaces(text: string) returns (result: string)
  ensures result == FixSpacesSpec(text, 0)
{
  result := FixSpacesAux(text, 0);
}

method FixSpacesAux(text: string, pendingSpaces: nat) returns (result: string)
  ensures result == FixSpacesSpec(text, pendingSpaces)
  decreases |text|
{
  if |text| == 0 {
    result := SpaceRunSpec(pendingSpaces);
  } else if text[0] == ' ' {
    result := FixSpacesAux(text[1..], pendingSpaces + 1);
  } else {
    var rest := FixSpacesAux(text[1..], 0);
    result := SpaceRunSpec(pendingSpaces) + text[0..1] + rest;
  }
}
