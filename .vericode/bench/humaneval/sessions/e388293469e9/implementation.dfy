function DigitName(d: int): string
{
  if d == 1 then "One"
  else if d == 2 then "Two"
  else if d == 3 then "Three"
  else if d == 4 then "Four"
  else if d == 5 then "Five"
  else if d == 6 then "Six"
  else if d == 7 then "Seven"
  else if d == 8 then "Eight"
  else if d == 9 then "Nine"
  else ""
}

function InsertDesc(d: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [d]
  else if d >= s[0] then [d] + s
  else [s[0]] + InsertDesc(d, s[1..])
}

function SortValidDesc(arr: seq<int>): seq<int>
  decreases |arr|
{
  if |arr| == 0 then []
  else
    var rest := SortValidDesc(arr[1..]);
    if 1 <= arr[0] && arr[0] <= 9 then InsertDesc(arr[0], rest) else rest
}

function MapDigitsToNames(digits: seq<int>): seq<string>
  decreases |digits|
{
  if |digits| == 0 then []
  else [DigitName(digits[0])] + MapDigitsToNames(digits[1..])
}

function ByLengthSpec(arr: seq<int>): seq<string>
{
  MapDigitsToNames(SortValidDesc(arr))
}

method by_length(arr: seq<int>) returns (result: seq<string>)
  ensures result == ByLengthSpec(arr)
{
  result := ByLengthSpec(arr);
}
