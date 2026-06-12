datatype MaybeInt = NoneInt | SomeInt(value: int)

function UpdateNegative(x: int, current: MaybeInt): MaybeInt
{
  if x < 0 then
    if current.NoneInt? then SomeInt(x)
    else if x > current.value then SomeInt(x)
    else current
  else current
}

function UpdatePositive(x: int, current: MaybeInt): MaybeInt
{
  if x > 0 then
    if current.NoneInt? then SomeInt(x)
    else if x < current.value then SomeInt(x)
    else current
  else current
}

function LargestSmallestIntegersSpec(lst: seq<int>): (MaybeInt, MaybeInt)
  decreases |lst|
{
  if |lst| == 0 then (NoneInt, NoneInt)
  else
    var tail := LargestSmallestIntegersSpec(lst[1..]);
    (UpdateNegative(lst[0], tail.0), UpdatePositive(lst[0], tail.1))
}

method largest_smallest_integers(lst: seq<int>) returns (result: (MaybeInt, MaybeInt))
  ensures result == LargestSmallestIntegersSpec(lst)
  decreases |lst|
{
  if |lst| == 0 {
    result := (NoneInt, NoneInt);
  } else {
    var tail := largest_smallest_integers(lst[1..]);
    result := (UpdateNegative(lst[0], tail.0), UpdatePositive(lst[0], tail.1));
  }
}
