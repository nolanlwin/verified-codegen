function ReverseDigitsAux(x: int, acc: int): int
  decreases x
{
  if x == 0 then acc
  else ReverseDigitsAux(x / 10, acc * 10 + x % 10)
}

function IsDecimalPalindrome(x: int): bool
{
  ReverseDigitsAux(x, 0) == x
}

function CountEvenOddPalindromesAux(i: int, n: int): (int, int)
  decreases n - i + 1
{
  if i > n then (0, 0)
  else
    var rest := CountEvenOddPalindromesAux(i + 1, n);
    if IsDecimalPalindrome(i) then
      if i % 2 == 0 then (rest.0 + 1, rest.1)
      else (rest.0, rest.1 + 1)
    else rest
}

function EvenOddPalindromeSpec(n: int): (int, int)
{
  CountEvenOddPalindromesAux(1, n)
}

method even_odd_palindrome(n: int) returns (result: (int, int))
  requires 1 <= n <= 1000
  ensures result == EvenOddPalindromeSpec(n)
{
  result := CountEvenOddPalindromesAuxMethod(1, n);
}

method CountEvenOddPalindromesAuxMethod(i: int, n: int) returns (r: (int, int))
  requires 1 <= i <= n + 1
  ensures r == CountEvenOddPalindromesAux(i, n)
  decreases n - i + 1
{
  if i > n {
    r := (0, 0);
  } else {
    var rest := CountEvenOddPalindromesAuxMethod(i + 1, n);
    if IsDecimalPalindrome(i) {
      if i % 2 == 0 {
        r := (rest.0 + 1, rest.1);
      } else {
        r := (rest.0, rest.1 + 1);
      }
    } else {
      r := rest;
    }
  }
}
