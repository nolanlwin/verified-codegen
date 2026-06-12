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
  var maxCount := MaxCountAuxMethod(test, test);
  result := HistogramBuildMethod(test, test, maxCount);
}

method CountLetterMethod(s: string, letter: string) returns (count: int)
  ensures count == CountLetter(s, letter)
  decreases |s|
{
  if |s| == 0 {
    count := 0;
  } else {
    var tail := CountLetterMethod(s[1..], letter);
    if s[0] != ' ' && s[0..1] == letter {
      count := 1 + tail;
    } else {
      count := tail;
    }
  }
}

method MaxCountAuxMethod(original: string, rest: string) returns (maxCount: int)
  ensures maxCount == MaxCountAux(original, rest)
  decreases |rest|
{
  if |rest| == 0 {
    maxCount := 0;
  } else {
    var tailMax := MaxCountAuxMethod(original, rest[1..]);
    if rest[0] == ' ' {
      maxCount := tailMax;
    } else {
      var count := CountLetterMethod(original, rest[0..1]);
      if count >= tailMax {
        maxCount := count;
      } else {
        maxCount := tailMax;
      }
    }
  }
}

method HistogramBuildMethod(original: string, rest: string, maxCount: int) returns (result: map<string, int>)
  ensures result == HistogramBuild(original, rest, maxCount)
  decreases |rest|
{
  if |rest| == 0 {
    result := map[];
  } else {
    var tail := HistogramBuildMethod(original, rest[1..], maxCount);
    if rest[0] == ' ' {
      result := tail;
    } else {
      var letter := rest[0..1];
      var count := CountLetterMethod(original, letter);
      if maxCount > 0 && count == maxCount {
        result := tail[letter := count];
      } else {
        result := tail;
      }
    }
  }
}
