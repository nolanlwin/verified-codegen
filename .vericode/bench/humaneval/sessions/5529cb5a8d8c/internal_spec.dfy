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
  []
}
