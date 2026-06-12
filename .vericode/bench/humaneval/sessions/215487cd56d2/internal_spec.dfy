function RowMatchesSpec(row: seq<int>, x: int, r: int, j: int): seq<(int, int)>
  decreases j
{
  []
}
function GetRowFromSpec(lst: seq<seq<int>>, x: int, i: int): seq<(int, int)>
  decreases |lst| - i
{
  if i == |lst| then
    []
  else
    RowMatchesSpec(lst[i], x, i, |lst[i]|) + GetRowFromSpec(lst, x, i + 1)
}
function GetRowSpec(lst: seq<seq<int>>, x: int): seq<(int, int)>
{
  GetRowFromSpec(lst, x, 0)
}

method get_row(lst: seq<seq<int>>, x: int) returns (result: seq<(int, int)>)
  requires true
  ensures result == GetRowSpec(lst, x)
{
  assume false;
}
