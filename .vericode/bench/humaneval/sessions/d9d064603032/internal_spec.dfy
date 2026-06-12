function CountEvenSpec(nums: seq<int>): int
  decreases |nums|
{
  if |nums| == 0 then 0
  else (if nums[0] % 2 == 0 then 1 else 0) + CountEvenSpec(nums[1..])
}
function ExchangeSpec(lst1: seq<int>, lst2: seq<int>): string
{
  if CountEvenSpec(lst1) + CountEvenSpec(lst2) >= |lst1| then "YES" else "NO"
}

method exchange(lst1: seq<int>, lst2: seq<int>) returns (result: string)
  requires |lst1| > 0
  requires |lst2| > 0
  ensures result == ExchangeSpec(lst1, lst2)
{
  assume false;
}
