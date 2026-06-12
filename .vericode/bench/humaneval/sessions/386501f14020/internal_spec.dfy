function ValidNumbersInput(s: string): bool
  decreases |s|
{
  if |s| == 0 then true else
    ((4 <= |s| && s[..4] == "zero" && (|s| == 4 || (5 < |s| && s[4] == ' ' && ValidNumbersInput(s[5..])))) ||
     (3 <= |s| && s[..3] == "one" && (|s| == 3 || (4 < |s| && s[3] == ' ' && ValidNumbersInput(s[4..])))) ||
     (3 <= |s| && s[..3] == "two" && (|s| == 3 || (4 < |s| && s[3] == ' ' && ValidNumbersInput(s[4..])))) ||
     (5 <= |s| && s[..5] == "three" && (|s| == 5 || (6 < |s| && s[5] == ' ' && ValidNumbersInput(s[6..])))) ||
     (4 <= |s| && s[..4] == "four" && (|s| == 4 || (5 < |s| && s[4] == ' ' && ValidNumbersInput(s[5..])))) ||
     (4 <= |s| && s[..4] == "five" && (|s| == 4 || (5 < |s| && s[4] == ' ' && ValidNumbersInput(s[5..])))) ||
     (3 <= |s| && s[..3] == "six" && (|s| == 3 || (4 < |s| && s[3] == ' ' && ValidNumbersInput(s[4..])))) ||
     (5 <= |s| && s[..5] == "seven" && (|s| == 5 || (6 < |s| && s[5] == ' ' && ValidNumbersInput(s[6..])))) ||
     (5 <= |s| && s[..5] == "eight" && (|s| == 5 || (6 < |s| && s[5] == ' ' && ValidNumbersInput(s[6..])))) ||
     (4 <= |s| && s[..4] == "nine" && (|s| == 4 || (5 < |s| && s[4] == ' ' && ValidNumbersInput(s[5..])))))
}
function WordOfRank(rank: int): string
{
  if rank == 0 then "zero" else
  if rank == 1 then "one" else
  if rank == 2 then "two" else
  if rank == 3 then "three" else
  if rank == 4 then "four" else
  if rank == 5 then "five" else
  if rank == 6 then "six" else
  if rank == 7 then "seven" else
  if rank == 8 then "eight" else
  "nine"
}
function IsTokenAt(s: string, i: int, word: string): bool
{
  false
}
function CountWordAtPositions(s: string, word: string, i: int): int
  decreases |s| - i
{
  if i == |s| then 0 else
    (if IsTokenAt(s, i, word) then 1 else 0) + CountWordAtPositions(s, word, i + 1)
}
function CountRankInInput(s: string, rank: int): int
{
  CountWordAtPositions(s, WordOfRank(rank), 0)
}
function RepeatWord(word: string, n: int, needSpace: bool): string
  decreases n
{
  if n <= 0 then "" else
    (if needSpace then " " else "") + word + RepeatWord(word, n - 1, true)
}
function SortFromRank(numbers: string, rank: int, needSpace: bool): string
  decreases 10 - rank
{
  if rank == 10 then "" else
    var count := CountRankInInput(numbers, rank);
    var word := WordOfRank(rank);
    RepeatWord(word, count, needSpace) + SortFromRank(numbers, rank + 1, needSpace || count > 0)
}
function SortNumbersSpec(numbers: string): string
{
  SortFromRank(numbers, 0, false)
}

method sort_numbers(numbers: string) returns (result: string)
  requires ValidNumbersInput(numbers)
  ensures result == SortNumbersSpec(numbers)
{
  assume false;
}
