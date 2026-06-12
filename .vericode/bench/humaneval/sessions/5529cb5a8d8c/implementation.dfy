function HasDivisorFrom(x: int, d: int): bool
  decreases x - d
{
  if d >= x then false else if x % d == 0 then true else HasDivisorFrom(x, d + 1)
}

function IsPrime(x: int): bool
{
  if x <= 1 then false else !HasDivisorFrom(x, 2)
}

function CountUpToSpec(n: int): seq<int>
  decreases n
{
  if n <= 0 then []
  else
    var previous := CountUpToSpec(n - 1);
    if IsPrime(n - 1) then previous + [n - 1] else previous
}

method count_up_to(n: int) returns (result: seq<int>)
  requires n >= 0
  ensures result == CountUpToSpec(n)
  decreases n
{
  if n == 0 {
    result := [];
  } else {
    var previous := count_up_to(n - 1);
    if IsPrime(n - 1) {
      result := previous + [n - 1];
    } else {
      result := previous;
    }
  }
}
