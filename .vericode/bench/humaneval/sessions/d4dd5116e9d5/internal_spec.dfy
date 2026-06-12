function MinInt(a: int, b: int): int
{
  if a <= b then a else b
}
function MinPrefixSumSpec(nums: seq<int>): int
  decreases |nums|
{
  if |nums| == 1 then nums[0]
  else
    var tailMinPrefix := MinPrefixSumSpec(nums[1..]);
    MinInt(nums[0], nums[0] + tailMinPrefix)
}
function MinsubarraysumSpec(nums: seq<int>): int
  decreases |nums|
{
  if |nums| == 1 then nums[0]
  else
    var startAtFirst := MinPrefixSumSpec(nums);
    var inTail := MinsubarraysumSpec(nums[1..]);
    MinInt(startAtFirst, inTail)
}

method minSubArraySum(nums: seq<int>) returns (result: int)
  requires |nums| > 0
  ensures result == MinsubarraysumSpec(nums)
{
  assume false;
}
