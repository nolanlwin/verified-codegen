function HasDivisorFromSpec(n: int, d: int): bool
  decreases if d < n then n - d else 0
{
  if d >= n then false
  else if n % d == 0 then true
  else HasDivisorFromSpec(n, d + 1)
}

function IsPrimeSpec(n: int): bool
{
  if n < 2 then false
  else !HasDivisorFromSpec(n, 2)
}

function EmitWordSpec(word: string, hasPrevious: bool): string
{
  if IsPrimeSpec(|word|) then
    if hasPrevious then " " + word else word
  else ""
}

function WordsInSentenceSpec(sentence: string, current: string, hasPrevious: bool): string
  decreases |sentence|
{
  if |sentence| == 0 then EmitWordSpec(current, hasPrevious)
  else if sentence[0] == ' ' then
    EmitWordSpec(current, hasPrevious) + WordsInSentenceSpec(sentence[1..], "", hasPrevious || IsPrimeSpec(|current|))
  else
    WordsInSentenceSpec(sentence[1..], current + [sentence[0]], hasPrevious)
}

method words_in_sentence(sentence: string) returns (result: string)
  ensures result == WordsInSentenceSpec(sentence, "", false)
{
  result := WordsInSentenceSpec(sentence, "", false);
}
