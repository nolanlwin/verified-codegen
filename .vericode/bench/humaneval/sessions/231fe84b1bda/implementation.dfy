function Count(numbers: seq<int>, x: int): int
  decreases |numbers|
{
  if |numbers| == 0 then
    0
  else
    (if numbers[0] == x then 1 else 0) + Count(numbers[1..], x)
}

function RemoveDuplicatesSpec(numbers: seq<int>): seq<int>
  decreases |numbers|
{
  if |numbers| == 0 then
    []
  else if Count(numbers, numbers[0]) == 1 then
    [numbers[0]] + RemoveDuplicatesSpec(numbers[1..])
  else
    RemoveDuplicatesSpec(numbers[1..])
}

method remove_duplicates(numbers: seq<int>) returns (result: seq<int>)
  requires true
  ensures result == RemoveDuplicatesSpec(numbers)
  decreases |numbers|
{
  if |numbers| == 0 {
    result := [];
  } else {
    var tailResult := remove_duplicates(numbers[1..]);
    if Count(numbers, numbers[0]) == 1 {
      result := [numbers[0]] + tailResult;
    } else {
      result := tailResult;
    }
  }
}
