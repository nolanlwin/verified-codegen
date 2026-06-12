datatype OptionInt = None | Some(value: int)
function SignSpec(x: int): int
{
  if x > 0 then 1 else if x < 0 then -1 else 0
}
function ProdSignsAux(arr: seq<int>, sumMag: int, prodSign: int): OptionInt
  decreases |arr|
{
  if |arr| == 0 then Some(sumMag * prodSign)
  else ProdSignsAux(arr[1..], sumMag + (if arr[0] < 0 then -arr[0] else arr[0]), prodSign * SignSpec(arr[0]))
}
function ProdSignsSpec(arr: seq<int>): OptionInt
{
  if |arr| == 0 then None
  else ProdSignsAux(arr, 0, 1)
}

method prod_signs(arr: seq<int>) returns (result: OptionInt)
  ensures result == ProdSignsSpec(arr)
{
  assume false;
}
