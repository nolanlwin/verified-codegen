function StartsOneEndsSpec(n: int): int
  decreases n
{
  if n == 1 then 1 else if n == 2 then 18 else 10 * StartsOneEndsSpec(n - 1)
}

method starts_one_ends(n: int) returns (result: int)
  requires n > 0
  ensures result == StartsOneEndsSpec(n)
  decreases n
{
  if n == 1 {
    result := 1;
  } else if n == 2 {
    result := 18;
  } else {
    var r := starts_one_ends(n - 1);
    result := 10 * r;
  }
}
