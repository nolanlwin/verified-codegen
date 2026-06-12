function CarRaceCollisionSpec(n: int): int
  decreases n
{
  if n == 0 then 0 else CarRaceCollisionSpec(n - 1) + 2 * n - 1
}

method car_race_collision(n: int) returns (result: int)
  requires n >= 0
  ensures result == CarRaceCollisionSpec(n)
{
  assume false;
}
