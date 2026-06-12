function LexLeq(a: string, b: string): bool
  decreases |a| + |b|
{
  if |a| == 0 then true
  else if |b| == 0 then false
  else if a[0] < b[0] then true
  else if b[0] < a[0] then false
  else LexLeq(a[1..], b[1..])
}

function WordLeq(a: string, b: string): bool
{
  if |a| < |b| then true
  else if |a| > |b| then false
  else LexLeq(a, b)
}

function InsertSorted(w: string, s: seq<string>): seq<string>
  decreases |s|
{
  if |s| == 0 || WordLeq(w, s[0]) then [w] + s
  else [s[0]] + InsertSorted(w, s[1..])
}

function SortedListSumSpec(lst: seq<string>): seq<string>
  decreases |lst|
{
  if |lst| == 0 then []
  else if |lst[0]| % 2 == 1 then SortedListSumSpec(lst[1..])
  else InsertSorted(lst[0], SortedListSumSpec(lst[1..]))
}

method sorted_list_sum(lst: seq<string>) returns (result: seq<string>)
  ensures result == SortedListSumSpec(lst)
  decreases |lst|
{
  if |lst| == 0 {
    result := [];
  } else if |lst[0]| % 2 == 1 {
    result := sorted_list_sum(lst[1..]);
  } else {
    var tail := sorted_list_sum(lst[1..]);
    result := InsertSorted(lst[0], tail);
  }
}
