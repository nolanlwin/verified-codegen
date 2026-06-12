function DigitSumNonNegative(n: int): int
  decreases n
{
  if n < 10 then n
  else n % 10 + DigitSumNonNegative(n / 10)
}

function LeadingDigitNonNegative(n: int): int
  decreases n
{
  if n < 10 then n
  else LeadingDigitNonNegative(n / 10)
}

function SignedDigitSumSpec(n: int): int
{
  if n >= 0 then DigitSumNonNegative(n)
  else DigitSumNonNegative(-n) - 2 * LeadingDigitNonNegative(-n)
}

function CountNumsSpec(arr: seq<int>): int
  decreases |arr|
{
  if |arr| == 0 then 0
  else (if SignedDigitSumSpec(arr[0]) > 0 then 1 else 0) + CountNumsSpec(arr[1..])
}

method count_nums(arr: seq<int>) returns (result: int)
  ensures result == CountNumsSpec(arr)
  decreases |arr|
{
  if |arr| == 0 {
    result := 0;
  } else {
    var tailResult := count_nums(arr[1..]);
    if SignedDigitSumSpec(arr[0]) > 0 {
      result := 1 + tailResult;
    } else {
      result := tailResult;
    }
  }
}
