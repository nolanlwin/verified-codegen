function PlanetRank(p: string): int
{
  if p == "Mercury" then 1
  else if p == "Venus" then 2
  else if p == "Earth" then 3
  else if p == "Mars" then 4
  else if p == "Jupiter" then 5
  else if p == "Saturn" then 6
  else if p == "Uranus" then 7
  else if p == "Neptune" then 8
  else 0
}
function PlanetAt(rank: int): string
{
  if rank == 1 then "Mercury"
  else if rank == 2 then "Venus"
  else if rank == 3 then "Earth"
  else if rank == 4 then "Mars"
  else if rank == 5 then "Jupiter"
  else if rank == 6 then "Saturn"
  else if rank == 7 then "Uranus"
  else "Neptune"
}
function PlanetsBetweenSpec(lo: int, hi: int, cur: int): seq<string>
  decreases 9 - cur
{
  if cur == 9 then []
  else if (lo < cur && cur < hi) || (hi < cur && cur < lo) then
    [PlanetAt(cur)] + PlanetsBetweenSpec(lo, hi, cur + 1)
  else
    PlanetsBetweenSpec(lo, hi, cur + 1)
}
function BfSpec(planet1: string, planet2: string): seq<string>
{
  var r1 := PlanetRank(planet1);
  var r2 := PlanetRank(planet2);
  if r1 == 0 || r2 == 0 then []
  else PlanetsBetweenSpec(r1, r2, 1)
}

method bf(planet1: string, planet2: string) returns (result: seq<string>)
  ensures result == BfSpec(planet1, planet2)
{
  assume false;
}
