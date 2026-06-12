function IscubeSearch(n: int, i: int): bool
  decreases n - i + 1
{
  if i > n then false
  else if i * i * i == n then true
  else IscubeSearch(n, i + 1)
}

function IscubeSpec(a: int): bool
{
  if a < 0 then IscubeSearch(-a, 0) else IscubeSearch(a, 0)
}

method iscube(a: int) returns (result: bool)
  requires true
  ensures result == IscubeSpec(a)
{
  if a < 0 {
    result := IscubeSearchMethod(-a, 0);
  } else {
    result := IscubeSearchMethod(a, 0);
  }
}

method IscubeSearchMethod(n: int, i: int) returns (result: bool)
  ensures result == IscubeSearch(n, i)
  decreases n - i + 1
{
  if i > n {
    result := false;
  } else if i * i * i == n {
    result := true;
  } else {
    result := IscubeSearchMethod(n, i + 1);
  }
}
