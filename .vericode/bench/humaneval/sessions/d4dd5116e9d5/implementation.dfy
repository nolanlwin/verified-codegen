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
  decreases |nums|
{
  if |nums| == 1 {
    result := nums[0];
  } else {
    assert |nums| > 1;
    var startAtFirst := ComputeMinPrefixSum(nums);
    var inTail := minSubArraySum(nums[1..]);
    result := MinInt(startAtFirst, inTail);
  }
}

method ComputeMinPrefixSum(nums: seq<int>) returns (result: int)
  requires |nums| > 0
  ensures result == MinPrefixSumSpec(nums)
  decreases |nums|
{
  if |nums| == 1 {
    result := nums[0];
  } else {
    assert |nums| > 1;
    var tailMinPrefix := ComputeMinPrefixSum(nums[1..]);
    result := MinInt(nums[0], nums[0] + tailMinPrefix);
  }
}
