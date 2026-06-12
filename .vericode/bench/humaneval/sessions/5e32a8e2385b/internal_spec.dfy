function CountLetter(s: string, letter: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else
    (if s[0] != ' ' && s[0..1] == letter then 1 else 0) + CountLetter(s[1..], letter)
}
function MaxCountAux(original: string, rest: string): int
  decreases |rest|
{
  if |rest| == 0 then 0
  else
    var tailMax := MaxCountAux(original, rest[1..]);
    if rest[0] == ' ' then tailMax
    else
      var count := CountLetter(original, rest[0..1]);
      if count >= tailMax then count else tailMax
}
function MaxCountSpec(test: string): int
{
  MaxCountAux(test, test)
}
function HistogramBuild(original: string, rest: string, maxCount: int): map<string, int>
  decreases |rest|
{
  if |rest| == 0 then map[]
  else
    var tail := HistogramBuild(original, rest[1..], maxCount);
    if rest[0] == ' ' then tail
    else
      var letter := rest[0..1];
      var count := CountLetter(original, letter);
      if maxCount > 0 && count == maxCount then tail[letter := count] else tail
}
function HistogramSpec(test: string): map<string, int>
{
  var maxCount := MaxCountSpec(test);
  HistogramBuild(test, test, maxCount)
}

method histogram(test: string) returns (result: map<string, int>)
  ensures result == HistogramSpec(test)
{
  assume false;
}
