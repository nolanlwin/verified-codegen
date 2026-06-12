function InsertAsc(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x <= s[0] then [x] + s
  else [s[0]] + InsertAsc(x, s[1..])
}

function SortAsc(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertAsc(s[0], SortAsc(s[1..]))
}

function InsertDesc(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x >= s[0] then [x] + s
  else [s[0]] + InsertDesc(x, s[1..])
}

function SortDesc(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertDesc(s[0], SortDesc(s[1..]))
}

function SortArraySpec(a: seq<int>): seq<int>
{
  if |a| <= 1 then a
  else if (a[0] + a[|a| - 1]) % 2 == 1 then SortAsc(a)
  else SortDesc(a)
}

method SortArray(a: seq<int>) returns (result: seq<int>)
  requires forall i :: 0 <= i < |a| ==> 0 <= a[i]
  ensures result == SortArraySpec(a)
{
  if |a| <= 1 {
    result := a;
  } else if (a[0] + a[|a| - 1]) % 2 == 1 {
    result := SortAsc(a);
  } else {
    result := SortDesc(a);
  }
}
