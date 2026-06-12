function GetPositiveSpec(l: seq<int>): seq<int>
  decreases |l|
{
  if |l| == 0 then
    []
  else if l[0] > 0 then
    [l[0]] + GetPositiveSpec(l[1..])
  else
    GetPositiveSpec(l[1..])
}

method get_positive(l: seq<int>) returns (result: seq<int>)
  ensures result == GetPositiveSpec(l)
{
  assume false;
}
