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
  decreases |numbers|
{
  if |numbers| <= 1 {
    result := false;
  } else {
    var close := close_to_any(numbers[0], numbers[1..], threshold);
    var rest := has_close_elements(numbers[1..], threshold);
    result := close || rest;
  }
}

function AbsDistReal(a: real, b: real): real
{
  AbsReal(a - b)
}

method close_to_any(x: real, numbers: seq<real>, threshold: real) returns (result: bool)
  ensures result == CloseToAnySpec(x, numbers, threshold)
  decreases |numbers|
{
  if |numbers| == 0 {
    result := false;
  } else {
    var tailResult := close_to_any(x, numbers[1..], threshold);
    result := AbsDistReal(x, numbers[0]) < threshold || tailResult;
    assert AbsDistReal(x, numbers[0]) == AbsReal(x - numbers[0]);
  }
}
