function IsOddDigit(d: int): bool
{
  d == 1 || d == 3 || d == 5 || d == 7 || d == 9
}

function FirstDigit(n: int): int
  decreases n
{
  if n < 10 then n else FirstDigit(n / 10)
}

function SpecialNumberSpec(n: int): bool
{
  n > 10 && IsOddDigit(FirstDigit(n)) && IsOddDigit(n % 10)
}

function SpecialfilterSpec(nums: seq<int>): int
  decreases |nums|
{
  if |nums| == 0 then 0
  else if SpecialNumberSpec(nums[0]) then 1 + SpecialfilterSpec(nums[1..])
  else SpecialfilterSpec(nums[1..])
}

method specialFilter(nums: seq<int>) returns (result: int)
  ensures result == SpecialfilterSpec(nums)
  decreases |nums|
{
  if |nums| == 0 {
    result := 0;
  } else {
    var tailResult := specialFilter(nums[1..]);
    if SpecialNumberSpec(nums[0]) {
      result := 1 + tailResult;
    } else {
      result := tailResult;
    }
  }
}
