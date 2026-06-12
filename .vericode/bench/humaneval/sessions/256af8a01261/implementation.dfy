function SumRealSeq(numbers: seq<real>): real
  decreases |numbers|
{
  if |numbers| == 0 then 0.0 else numbers[0] + SumRealSeq(numbers[1..])
}

function AbsReal(x: real): real
{
  if x < 0.0 then -x else x
}

function SumAbsoluteDeviations(numbers: seq<real>, mean: real): real
  decreases |numbers|
{
  if |numbers| == 0 then 0.0 else AbsReal(numbers[0] - mean) + SumAbsoluteDeviations(numbers[1..], mean)
}

function MeanAbsoluteDeviationSpec(numbers: seq<real>): real
{
  var mean := SumRealSeq(numbers) / (|numbers| as real);
  SumAbsoluteDeviations(numbers, mean) / (|numbers| as real)
}

method mean_absolute_deviation(numbers: seq<real>) returns (result: real)
  requires |numbers| > 0
  ensures result == MeanAbsoluteDeviationSpec(numbers)
{
  result := MeanAbsoluteDeviationSpec(numbers);
}
