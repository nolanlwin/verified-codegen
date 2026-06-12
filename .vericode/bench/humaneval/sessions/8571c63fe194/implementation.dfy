function NatDigitSum(n: int): int
  decreases n
{
  if n < 10 then n
  else n % 10 + NatDigitSum(n / 10)
}

function NegativeDigitSum(m: int): int
  decreases m
{
  if m < 10 then -m
  else m % 10 + NegativeDigitSum(m / 10)
}

function PointValue(n: int): int
{
  if n >= 0 then NatDigitSum(n)
  else NegativeDigitSum(-n)
}

function InsertByPoint(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if PointValue(x) <= PointValue(s[0]) then [x] + s
  else [s[0]] + InsertByPoint(x, s[1..])
}

function OrderByPointsSpec(nums: seq<int>): seq<int>
  decreases |nums|
{
  if |nums| <= 1 then nums
  else InsertByPoint(nums[0], OrderByPointsSpec(nums[1..]))
}

method order_by_points(nums: seq<int>) returns (result: seq<int>)
  ensures result == OrderByPointsSpec(nums)
  decreases |nums|
{
  if |nums| <= 1 {
    result := nums;
  } else {
    var tail := order_by_points(nums[1..]);
    result := InsertByPointMethod(nums[0], tail);
  }
}

method InsertByPointMethod(x: int, s: seq<int>) returns (r: seq<int>)
  ensures r == InsertByPoint(x, s)
  decreases |s|
{
  if |s| == 0 {
    r := [x];
  } else if PointValue(x) <= PointValue(s[0]) {
    r := [x] + s;
  } else {
    var tail := InsertByPointMethod(x, s[1..]);
    r := [s[0]] + tail;
  }
}
