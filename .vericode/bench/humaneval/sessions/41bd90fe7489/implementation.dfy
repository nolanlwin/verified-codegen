datatype SplitWordsResult = Words(words: seq<string>) | Count(count: int)

function IsWhitespace(c: char): bool
{
  c == ' ' || c == '\t' || c == '\n' || c == '\r'
}

function ContainsWhitespace(s: string): bool
  decreases |s|
{
  if |s| == 0 then false
  else IsWhitespace(s[0]) || ContainsWhitespace(s[1..])
}

function ContainsComma(s: string): bool
  decreases |s|
{
  if |s| == 0 then false
  else s[0] == ',' || ContainsComma(s[1..])
}

function SplitWhitespaceScan(s: string, start: int, i: int): seq<string>
  decreases |s| - i
{
  if i == |s| then
    if start < i then [s[start..i]] else []
  else if IsWhitespace(s[i]) then
    if start < i then [s[start..i]] + SplitWhitespaceScan(s, i + 1, i + 1)
    else SplitWhitespaceScan(s, i + 1, i + 1)
  else SplitWhitespaceScan(s, start, i + 1)
}

function SplitOnWhitespaceSpec(s: string): seq<string>
{
  SplitWhitespaceScan(s, 0, 0)
}

function SplitCommaScan(s: string, start: int, i: int): seq<string>
  decreases |s| - i
{
  if i == |s| then
    if start < i then [s[start..i]] else []
  else if s[i] == ',' then
    if start < i then [s[start..i]] + SplitCommaScan(s, i + 1, i + 1)
    else SplitCommaScan(s, i + 1, i + 1)
  else SplitCommaScan(s, start, i + 1)
}

function SplitOnCommaSpec(s: string): seq<string>
{
  SplitCommaScan(s, 0, 0)
}

function IsOddOrderLowercase(c: char): bool
{
  c == 'b' || c == 'd' || c == 'f' || c == 'h' || c == 'j' || c == 'l' ||
  c == 'n' || c == 'p' || c == 'r' || c == 't' || c == 'v' || c == 'x' || c == 'z'
}

function CountOddLowercase(s: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else (if IsOddOrderLowercase(s[0]) then 1 else 0) + CountOddLowercase(s[1..])
}

function SplitWordsSpec(txt: string): SplitWordsResult
{
  if ContainsWhitespace(txt) then Words(SplitOnWhitespaceSpec(txt))
  else if ContainsComma(txt) then Words(SplitOnCommaSpec(txt))
  else Count(CountOddLowercase(txt))
}

method split_words(txt: string) returns (result: SplitWordsResult)
  ensures result == SplitWordsSpec(txt)
{
  var hasWhitespace := ContainsWhitespaceMethod(txt);
  if hasWhitespace {
    assert ContainsWhitespace(txt);
    var ws := SplitWhitespaceScanMethod(txt, 0, 0);
    assert ws == SplitOnWhitespaceSpec(txt);
    result := Words(ws);
  } else {
    assert !ContainsWhitespace(txt);
    var hasComma := ContainsCommaMethod(txt);
    if hasComma {
      assert ContainsComma(txt);
      var parts := SplitCommaScanMethod(txt, 0, 0);
      assert parts == SplitOnCommaSpec(txt);
      result := Words(parts);
    } else {
      assert !ContainsComma(txt);
      var n := CountOddLowercaseMethod(txt);
      assert n == CountOddLowercase(txt);
      result := Count(n);
    }
  }
}

method ContainsWhitespaceMethod(s: string) returns (r: bool)
  ensures r == ContainsWhitespace(s)
  decreases |s|
{
  if |s| == 0 {
    r := false;
  } else {
    var tail := ContainsWhitespaceMethod(s[1..]);
    r := IsWhitespace(s[0]) || tail;
  }
}

method ContainsCommaMethod(s: string) returns (r: bool)
  ensures r == ContainsComma(s)
  decreases |s|
{
  if |s| == 0 {
    r := false;
  } else {
    var tail := ContainsCommaMethod(s[1..]);
    r := s[0] == ',' || tail;
  }
}

method CountOddLowercaseMethod(s: string) returns (r: int)
  ensures r == CountOddLowercase(s)
  decreases |s|
{
  if |s| == 0 {
    r := 0;
  } else {
    var tail := CountOddLowercaseMethod(s[1..]);
    r := (if IsOddOrderLowercase(s[0]) then 1 else 0) + tail;
  }
}

method SplitWhitespaceScanMethod(s: string, start: int, i: int) returns (r: seq<string>)
  requires 0 <= start <= i <= |s|
  ensures r == SplitWhitespaceScan(s, start, i)
  decreases |s| - i
{
  if i == |s| {
    if start < i {
      r := [s[start..i]];
    } else {
      r := [];
    }
  } else {
    assert i < |s|;
    if IsWhitespace(s[i]) {
      if start < i {
        var rest := SplitWhitespaceScanMethod(s, i + 1, i + 1);
        r := [s[start..i]] + rest;
      } else {
        r := SplitWhitespaceScanMethod(s, i + 1, i + 1);
      }
    } else {
      r := SplitWhitespaceScanMethod(s, start, i + 1);
    }
  }
}

method SplitCommaScanMethod(s: string, start: int, i: int) returns (r: seq<string>)
  requires 0 <= start <= i <= |s|
  ensures r == SplitCommaScan(s, start, i)
  decreases |s| - i
{
  if i == |s| {
    if start < i {
      r := [s[start..i]];
    } else {
      r := [];
    }
  } else {
    assert i < |s|;
    if s[i] == ',' {
      if start < i {
        var rest := SplitCommaScanMethod(s, i + 1, i + 1);
        r := [s[start..i]] + rest;
      } else {
        r := SplitCommaScanMethod(s, i + 1, i + 1);
      }
    } else {
      r := SplitCommaScanMethod(s, start, i + 1);
    }
  }
}
