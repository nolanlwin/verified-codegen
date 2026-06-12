function InsertAsc(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x <= s[0] then [x] + s
  else [s[0]] + InsertAsc(x, s[1..])
}
function SortAsc(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertAsc(s[0], SortAsc(s[1..]))
}
function InsertDesc(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x >= s[0] then [x] + s
  else [s[0]] + InsertDesc(x, s[1..])
}
function SortDesc(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertDesc(s[0], SortDesc(s[1..]))
}
function SortArraySpec(a: seq<int>): seq<int>
{
  []
}
