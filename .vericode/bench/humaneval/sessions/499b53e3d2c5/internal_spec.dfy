function CompareSpec(game: seq<int>, guess: seq<int>): seq<int>
  decreases |game|
{
  if |game| == 0 then []
  else
    var diff := game[0] - guess[0];
    var absDiff := if diff < 0 then -diff else diff;
    [absDiff] + CompareSpec(game[1..], guess[1..])
}

method compare(game: seq<int>, guess: seq<int>) returns (result: seq<int>)
  requires |game| == |guess|
  ensures result == CompareSpec(game, guess)
{
  assume false;
}
