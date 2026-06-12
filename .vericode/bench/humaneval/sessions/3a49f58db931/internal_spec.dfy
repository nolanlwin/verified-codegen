datatype Position = Position(row: int, col: int)
function IsSquareGrid(grid: seq<seq<int>>): bool
{
  |grid| >= 2 &&
  (forall i: int :: 0 <= i && i < |grid| ==> |grid[i]| == |grid|)
}
function InBounds(grid: seq<seq<int>>, r: int, c: int): bool
{
  0 <= r && r < |grid| && 0 <= c && c < |grid|
}
function ValuesInRangeUnique(grid: seq<seq<int>>): bool
{
  (forall r: int, c: int ::
    0 <= r && r < |grid| && 0 <= c && c < |grid| ==>
      1 <= grid[r][c] && grid[r][c] <= |grid| * |grid|) &&
  (forall r1: int, c1: int, r2: int, c2: int ::
    0 <= r1 && r1 < |grid| && 0 <= c1 && c1 < |grid| &&
    0 <= r2 && r2 < |grid| && 0 <= c2 && c2 < |grid| &&
    grid[r1][c1] == grid[r2][c2] ==>
      r1 == r2 && c1 == c2)
}
function ValidGrid(grid: seq<seq<int>>): bool
{
  IsSquareGrid(grid) && ValuesInRangeUnique(grid)
}
function CellValueOrLarge(grid: seq<seq<int>>, r: int, c: int): int
{
  if InBounds(grid, r, c) then grid[r][c] else |grid| * |grid| + 1
}
function ValueAtIndex(grid: seq<seq<int>>, index: int): int
{
  grid[index / |grid|][index % |grid|]
}
function PositionAtIndex(grid: seq<seq<int>>, index: int): Position
{
  Position(index / |grid|, index % |grid|)
}
function MinIndexFrom(grid: seq<seq<int>>, index: int): int
  decreases |grid| * |grid| - index
{
  if index == |grid| * |grid| - 1 then index
  else
    var tail := MinIndexFrom(grid, index + 1);
    if ValueAtIndex(grid, index) <= ValueAtIndex(grid, tail) then index else tail
}
function MinPosition(grid: seq<seq<int>>): Position
{
  PositionAtIndex(grid, MinIndexFrom(grid, 0))
}
function NeighborValueOrLarge(grid: seq<seq<int>>, r: int, c: int, dir: int): int
{
  if dir == 0 then CellValueOrLarge(grid, r - 1, c)
  else if dir == 1 then CellValueOrLarge(grid, r + 1, c)
  else if dir == 2 then CellValueOrLarge(grid, r, c - 1)
  else if dir == 3 then CellValueOrLarge(grid, r, c + 1)
  else |grid| * |grid| + 1
}
function MinNeighborDirFrom(grid: seq<seq<int>>, r: int, c: int, dir: int): int
  decreases 4 - dir
{
  if dir == 3 then dir
  else
    var tail := MinNeighborDirFrom(grid, r, c, dir + 1);
    if NeighborValueOrLarge(grid, r, c, dir) <= NeighborValueOrLarge(grid, r, c, tail) then dir else tail
}
function NeighborPosition(grid: seq<seq<int>>, r: int, c: int, dir: int): Position
{
  if dir == 0 then Position(r - 1, c)
  else if dir == 1 then Position(r + 1, c)
  else if dir == 2 then Position(r, c - 1)
  else Position(r, c + 1)
}
function MinNeighborPosition(grid: seq<seq<int>>, r: int, c: int): Position
{
  var dir := MinNeighborDirFrom(grid, r, c, 0);
  NeighborPosition(grid, r, c, dir)
}
function MinpathFrom(grid: seq<seq<int>>, r: int, c: int, k: int): seq<int>
  decreases k
{
  if k == 1 then [CellValueOrLarge(grid, r, c)]
  else
    var next := MinNeighborPosition(grid, r, c);
    [CellValueOrLarge(grid, r, c)] + MinpathFrom(grid, next.row, next.col, k - 1)
}
function MinpathSpec(grid: seq<seq<int>>, k: int): seq<int>
{
  var start := MinPosition(grid);
  MinpathFrom(grid, start.row, start.col, k)
}

method minPath(grid: seq<seq<int>>, k: int) returns (result: seq<int>)
  requires ValidGrid(grid)
  requires k > 0
  ensures result == MinpathSpec(grid, k)
{
  assume false;
}
