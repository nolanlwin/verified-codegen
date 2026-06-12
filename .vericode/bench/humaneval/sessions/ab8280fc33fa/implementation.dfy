function TriplesSumToZeroSpec(l: seq<int>): bool
{
  ExistsTripleI(l, 0)
}

function ExistsTripleI(l: seq<int>, i: int): bool
  decreases |l| - i
{
  if i >= |l| then
    false
  else
    ExistsTripleJ(l, i, i + 1) || ExistsTripleI(l, i + 1)
}

function ExistsTripleJ(l: seq<int>, i: int, j: int): bool
  decreases |l| - j
{
  if j >= |l| then
    false
  else
    ExistsTripleK(l, i, j, j + 1) || ExistsTripleJ(l, i, j + 1)
}

function ExistsTripleK(l: seq<int>, i: int, j: int, k: int): bool
  decreases |l| - k
{
  if k >= |l| then
    false
  else
    l[i] + l[j] + l[k] == 0 || ExistsTripleK(l, i, j, k + 1)
}

method triples_sum_to_zero(l: seq<int>) returns (result: bool)
  ensures result == TriplesSumToZeroSpec(l)
{
  result := ExistsTripleIMethod(l, 0);
}

method ExistsTripleKMethod(l: seq<int>, i: int, j: int, k: int) returns (result: bool)
  requires 0 <= i && i < |l|
  requires 0 <= j && j < |l|
  requires 0 <= k && k <= |l|
  requires i < j
  requires j < k
  ensures result == ExistsTripleK(l, i, j, k)
  decreases |l| - k
{
  if k >= |l| {
    result := false;
  } else if l[i] + l[j] + l[k] == 0 {
    result := true;
  } else {
    result := ExistsTripleKMethod(l, i, j, k + 1);
  }
}

method ExistsTripleJMethod(l: seq<int>, i: int, j: int) returns (result: bool)
  requires 0 <= i && i < |l|
  requires 0 <= j && j <= |l|
  requires i < j
  ensures result == ExistsTripleJ(l, i, j)
  decreases |l| - j
{
  if j >= |l| {
    result := false;
  } else {
    var kResult := ExistsTripleKMethod(l, i, j, j + 1);
    if kResult {
      result := true;
    } else {
      result := ExistsTripleJMethod(l, i, j + 1);
    }
  }
}

method ExistsTripleIMethod(l: seq<int>, i: int) returns (result: bool)
  requires 0 <= i && i <= |l|
  ensures result == ExistsTripleI(l, i)
  decreases |l| - i
{
  if i >= |l| {
    result := false;
  } else {
    var jResult := ExistsTripleJMethod(l, i, i + 1);
    if jResult {
      result := true;
    } else {
      result := ExistsTripleIMethod(l, i + 1);
    }
  }
}
