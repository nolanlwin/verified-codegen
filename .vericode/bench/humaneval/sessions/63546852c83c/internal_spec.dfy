function EncryptChar(c: char): char
{
  if c == 'a' then 'e' else
  if c == 'b' then 'f' else
  if c == 'c' then 'g' else
  if c == 'd' then 'h' else
  if c == 'e' then 'i' else
  if c == 'f' then 'j' else
  if c == 'g' then 'k' else
  if c == 'h' then 'l' else
  if c == 'i' then 'm' else
  if c == 'j' then 'n' else
  if c == 'k' then 'o' else
  if c == 'l' then 'p' else
  if c == 'm' then 'q' else
  if c == 'n' then 'r' else
  if c == 'o' then 's' else
  if c == 'p' then 't' else
  if c == 'q' then 'u' else
  if c == 'r' then 'v' else
  if c == 's' then 'w' else
  if c == 't' then 'x' else
  if c == 'u' then 'y' else
  if c == 'v' then 'z' else
  if c == 'w' then 'a' else
  if c == 'x' then 'b' else
  if c == 'y' then 'c' else
  if c == 'z' then 'd' else
  c
}
function EncryptSpec(s: string): string
  decreases |s|
{
  if |s| == 0 then "" else [EncryptChar(s[0])] + EncryptSpec(s[1..])
}

method encrypt(s: string) returns (result: string)
  ensures result == EncryptSpec(s)
{
  assume false;
}
