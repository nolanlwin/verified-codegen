function CountDigit7(x: int): int
  decreases x
{
  if x == 0 then 0 else (if x % 10 == 7 then 1 else 0) + CountDigit7(x / 10)
}

function FizzBuzzSpec(n: int): int
  decreases if n < 0 then 0 else n
{
  if n <= 0 then 0 else FizzBuzzSpec(n - 1) + (if (n - 1) % 11 == 0 || (n - 1) % 13 == 0 then CountDigit7(n - 1) else 0)
}

method fizz_buzz(n: int) returns (result: int)
  ensures result == FizzBuzzSpec(n)
  decreases if n < 0 then 0 else n
{
  if n <= 0 {
    result := 0;
  } else {
    var r := fizz_buzz(n - 1);
    result := r + (if (n - 1) % 11 == 0 || (n - 1) % 13 == 0 then CountDigit7(n - 1) else 0);
  }
}
