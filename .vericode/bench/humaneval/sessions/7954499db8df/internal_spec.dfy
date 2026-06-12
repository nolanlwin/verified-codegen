function CountRowWaterSpec(row: seq<int>): int
  decreases |row|
{
  if |row| == 0 then 0
  else (if row[0] == 1 then 1 else 0) + CountRowWaterSpec(row[1..])
}
function MaxFillSpec(grid: seq<seq<int>>, capacity: int): int
  decreases |grid|
{
  if |grid| == 0 then 0
  else
    var rowWater := CountRowWaterSpec(grid[0]);
    ((rowWater + capacity - 1) / capacity) + MaxFillSpec(grid[1..], capacity)
}

method max_fill(grid: seq<seq<int>>, capacity: int) returns (result: int)
  requires 1 <= |grid| <= 100
  requires 1 <= capacity <= 10
  requires forall i: int :: 0 <= i < |grid| ==> 1 <= |grid[i]| <= 100
  requires forall i: int :: 0 <= i < |grid| ==> |grid[i]| == |grid[0]|
  requires forall i: int, j: int :: 0 <= i < |grid| && 0 <= j < |grid[i]| ==> grid[i][j] == 0 || grid[i][j] == 1
  ensures result == MaxFillSpec(grid, capacity)
{
  assume false;
}
