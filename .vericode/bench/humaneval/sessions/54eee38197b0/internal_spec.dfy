function AbsReal(x: real): real
{
  if x < 0.0 then -x else x
}
function CloseToAnySpec(x: real, numbers: seq<real>, threshold: real): bool
  decreases |numbers|
{
  if |numbers| == 0 then false
  else AbsReal(x - numbers[0]) < threshold || CloseToAnySpec(x, numbers[1..], threshold)
}
function HasCloseElementsSpec(numbers: seq<real>, threshold: real): bool
  decreases |numbers|
{
  if |numbers| <= 1 then false
  else CloseToAnySpec(numbers[0], numbers[1..], threshold) || HasCloseElementsSpec(numbers[1..], threshold)
}

method has_close_elements(numbers: seq<real>, threshold: real) returns (result: bool)
  ensures result == HasCloseElementsSpec(numbers, threshold)
{
  assume false;
}
