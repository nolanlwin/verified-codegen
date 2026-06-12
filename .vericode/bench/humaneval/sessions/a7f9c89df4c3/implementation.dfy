function InsertSortedSpec(x: int, s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then [x]
  else if x <= s[0] then [x] + s
  else [s[0]] + InsertSortedSpec(x, s[1..])
}

function SortAscendingSpec(s: seq<int>): seq<int>
  decreases |s|
{
  if |s| == 0 then []
  else InsertSortedSpec(s[0], SortAscendingSpec(s[1..]))
}

function SuffixOfLengthSpec(s: seq<int>, k: int): seq<int>
  decreases |s|
{
  if |s| <= k then s
  else SuffixOfLengthSpec(s[1..], k)
}

function MaximumSpec(arr: seq<int>, k: int): seq<int>
  decreases |arr|
{
  if k == 0 then []
  else if k == |arr| then SortAscendingSpec(arr)
  else
    var rest := MaximumSpec(arr[1..], k);
    SuffixOfLengthSpec(InsertSortedSpec(arr[0], rest), k)
}

method maximum(arr: seq<int>, k: int) returns (result: seq<int>)
  requires 1 <= |arr| <= 1000
  requires 0 <= k <= |arr|
  requires forall i :: 0 <= i < |arr| ==> -1000 <= arr[i] <= 1000
  ensures result == MaximumSpec(arr, k)
  decreases |arr|
{
  if k == 0 {
    result := [];
    assert MaximumSpec(arr, k) == [];
  } else if k == |arr| {
    assert k != 0;
    assert |arr| != 0;
    result := SortAscending(arr);
    assert result == SortAscendingSpec(arr);
    assert MaximumSpec(arr, k) == SortAscendingSpec(arr);
  } else {
    assert 0 < k;
    assert k < |arr|;
    assert 2 <= |arr|;
    assert 1 <= |arr[1..]|;
    assert k <= |arr[1..]|;
    forall i | 0 <= i < |arr[1..]|
      ensures -1000 <= arr[1..][i] <= 1000
    {
      assert 0 <= i + 1 < |arr|;
      assert arr[1..][i] == arr[i + 1];
      assert -1000 <= arr[i + 1] <= 1000;
    }

    var rest := maximum(arr[1..], k);
    assert rest == MaximumSpec(arr[1..], k);
    var inserted := InsertSorted(arr[0], rest);
    assert inserted == InsertSortedSpec(arr[0], rest);
    assert inserted == InsertSortedSpec(arr[0], MaximumSpec(arr[1..], k));
    result := SuffixOfLength(inserted, k);
    assert result == SuffixOfLengthSpec(inserted, k);
    assert result == SuffixOfLengthSpec(InsertSortedSpec(arr[0], MaximumSpec(arr[1..], k)), k);
    assert k != 0;
    assert k != |arr|;
    assert 0 < |arr|;
    assert MaximumSpec(arr, k) == SuffixOfLengthSpec(InsertSortedSpec(arr[0], MaximumSpec(arr[1..], k)), k);
  }
}

method InsertSorted(x: int, s: seq<int>) returns (r: seq<int>)
  ensures r == InsertSortedSpec(x, s)
  decreases |s|
{
  if |s| == 0 {
    r := [x];
  } else if x <= s[0] {
    r := [x] + s;
  } else {
    var t := InsertSorted(x, s[1..]);
    r := [s[0]] + t;
  }
}

method SortAscending(s: seq<int>) returns (r: seq<int>)
  ensures r == SortAscendingSpec(s)
  decreases |s|
{
  if |s| == 0 {
    r := [];
  } else {
    var sortedTail := SortAscending(s[1..]);
    r := InsertSorted(s[0], sortedTail);
  }
}

method SuffixOfLength(s: seq<int>, k: int) returns (r: seq<int>)
  requires 0 <= k
  ensures r == SuffixOfLengthSpec(s, k)
  decreases |s|
{
  if |s| <= k {
    r := s;
  } else {
    assert 0 < |s|;
    r := SuffixOfLength(s[1..], k);
  }
}
