function IsDigitChar(c: char): bool
{
  c == '0' || c == '1' || c == '2' || c == '3' || c == '4' ||
  c == '5' || c == '6' || c == '7' || c == '8' || c == '9'
}

function DigitValue(c: char): int
{
  if c == '0' then 0
  else if c == '1' then 1
  else if c == '2' then 2
  else if c == '3' then 3
  else if c == '4' then 4
  else if c == '5' then 5
  else if c == '6' then 6
  else if c == '7' then 7
  else if c == '8' then 8
  else if c == '9' then 9
  else 0
}

function Pow10(n: int): int
  decreases n
{
  if n == 0 then 1 else 10 * Pow10(n - 1)
}

function ParseDigitsSpec(s: string): int
  decreases |s|
{
  if |s| == 0 then 0
  else DigitValue(s[0]) * Pow10(|s| - 1) + ParseDigitsSpec(s[1..])
}

function AllDigitsSpec(s: string): bool
  decreases |s|
{
  if |s| == 0 then true
  else IsDigitChar(s[0]) && AllDigitsSpec(s[1..])
}

function SlashIndexFromSpec(s: string, i: int): int
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then |s|
  else if s[i] == '/' then i
  else SlashIndexFromSpec(s, i + 1)
}

function FractionNumeratorSpec(s: string): int
{
  var slash := SlashIndexFromSpec(s, 0);
  ParseDigitsSpec(s[0..slash])
}

function FractionDenominatorSpec(s: string): int
{
  var slash := SlashIndexFromSpec(s, 0);
  if slash + 1 < |s| then ParseDigitsSpec(s[slash + 1..]) else 0
}

function ValidFractionStringSpec(s: string): bool
{
  var slash := SlashIndexFromSpec(s, 0);
  0 < slash && slash + 1 < |s| &&
  AllDigitsSpec(s[0..slash]) &&
  AllDigitsSpec(s[slash + 1..]) &&
  ParseDigitsSpec(s[0..slash]) > 0 &&
  ParseDigitsSpec(s[slash + 1..]) > 0
}

function SimplifySpec(x: string, n: string): bool
{
  var xNum := FractionNumeratorSpec(x);
  var xDen := FractionDenominatorSpec(x);
  var nNum := FractionNumeratorSpec(n);
  var nDen := FractionDenominatorSpec(n);
  (xNum * nNum) % (xDen * nDen) == 0
}

method simplify(x: string, n: string) returns (result: bool)
  requires ValidFractionStringSpec(x)
  requires ValidFractionStringSpec(n)
  ensures result == SimplifySpec(x, n)
{
  result := SimplifySpec(x, n);
}
