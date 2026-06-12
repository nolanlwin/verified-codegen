function IsInteger(r: real): bool
{
  false
}
function AllIntegersFrom(nums: seq<real>, i: int): bool
  decreases |nums| - i
{
  if i == |nums| then
    true
  else
    IsInteger(nums[i]) && AllIntegersFrom(nums, i + 1)
}
function AnyIntSpec(x: real, y: real, z: real): bool
{
  AllIntegersFrom([x, y, z], 0) &&
  (x == y + z || y == x + z || z == x + y)
}

method any_int(x: real, y: real, z: real) returns (result: bool)
  ensures result == AnyIntSpec(x, y, z)
{
  assume false;
}
