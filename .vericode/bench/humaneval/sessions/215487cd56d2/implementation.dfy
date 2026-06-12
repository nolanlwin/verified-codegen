function RowMatchesSpec(row: seq<int>, x: int, r: int, j: int): seq<(int, int)>
  decreases j
{
  if j <= 0 then
    []
  else if j > |row| then
    RowMatchesSpec(row, x, r, |row|)
  else
    (if row[j - 1] == x then [(r, j - 1)] else []) + RowMatchesSpec(row, x, r, j - 1)
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
  result := get_row_from(lst, x, 0);
}

method row_matches(row: seq<int>, x: int, r: int, j: int) returns (result: seq<(int, int)>)
  requires 0 <= j <= |row|
  ensures result == RowMatchesSpec(row, x, r, j)
  decreases j
{
  if j == 0 {
    result := [];
  } else {
    var tail := row_matches(row, x, r, j - 1);
    if row[j - 1] == x {
      result := [(r, j - 1)] + tail;
    } else {
      result := tail;
    }
  }
}

method get_row_from(lst: seq<seq<int>>, x: int, i: int) returns (result: seq<(int, int)>)
  requires 0 <= i <= |lst|
  ensures result == GetRowFromSpec(lst, x, i)
  decreases |lst| - i
{
  if i == |lst| {
    result := [];
  } else {
    var current := row_matches(lst[i], x, i, |lst[i]|);
    var rest := get_row_from(lst, x, i + 1);
    result := current + rest;
  }
}
