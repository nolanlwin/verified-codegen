datatype CompareValue = IntVal(i: int) | RealVal(r: real) | StringVal(s: string) | NoneVal

function IsDigit(c: char): bool
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
  else 9
}

function IsSeparator(c: char): bool
{
  c == '.' || c == ','
}

function AllNumberCharsFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then true
  else (IsDigit(s[i]) || IsSeparator(s[i])) && AllNumberCharsFrom(s, i + 1)
}

function ContainsDigitFrom(s: string, i: int): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then false
  else IsDigit(s[i]) || ContainsDigitFrom(s, i + 1)
}

function AtMostOneSeparatorFrom(s: string, i: int, seen: bool): bool
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then true
  else if IsSeparator(s[i]) then !seen && AtMostOneSeparatorFrom(s, i + 1, true)
  else AtMostOneSeparatorFrom(s, i + 1, seen)
}

function ValidUnsignedNumericString(s: string): bool
{
  |s| > 0 &&
  AllNumberCharsFrom(s, 0) &&
  ContainsDigitFrom(s, 0) &&
  AtMostOneSeparatorFrom(s, 0, false)
}

function ValidNumericString(s: string): bool
{
  if |s| == 0 then false
  else if s[0] == '-' then |s| > 1 && ValidUnsignedNumericString(s[1..])
  else ValidUnsignedNumericString(s)
}

function ParseUnsignedAux(s: string, i: int, seenSep: bool, num: int, scale: int): real
  decreases |s| - i
  requires 0 <= i <= |s|
{
  if i == |s| then (num as real) / (scale as real)
  else if IsSeparator(s[i]) then ParseUnsignedAux(s, i + 1, true, num, scale)
  else if seenSep then ParseUnsignedAux(s, i + 1, true, num * 10 + DigitValue(s[i]), scale * 10)
  else ParseUnsignedAux(s, i + 1, false, num * 10 + DigitValue(s[i]), scale)
}

function ParseNumericString(s: string): real
{
  if |s| == 0 then 0.0
  else if s[0] == '-' then -ParseUnsignedAux(s[1..], 0, false, 0, 1)
  else ParseUnsignedAux(s, 0, false, 0, 1)
}

function IsValidCompareValue(v: CompareValue): bool
{
  match v
  case IntVal(i) => true
  case RealVal(r) => true
  case StringVal(s) => ValidNumericString(s)
  case NoneVal => false
}

function CompareValueToReal(v: CompareValue): real
{
  match v
  case IntVal(i) => i as real
  case RealVal(r) => r
  case StringVal(s) => ParseNumericString(s)
  case NoneVal => 0.0
}

function CompareOneSpec(a: CompareValue, b: CompareValue): CompareValue
{
  var av := CompareValueToReal(a);
  var bv := CompareValueToReal(b);
  if av > bv then a else if bv > av then b else NoneVal
}

method compare_one(a: CompareValue, b: CompareValue) returns (result: CompareValue)
  requires IsValidCompareValue(a)
  requires IsValidCompareValue(b)
  ensures result == CompareOneSpec(a, b)
{
  result := CompareOneSpec(a, b);
}
