The function takes a sequence of non-negative integers and returns true exactly when the sequence is in ascending, nondecreasing order and no integer appears more than twice. Empty and single-element sequences are considered sorted. Adjacent equal pairs are allowed, but three equal values in a row make the result false.

Notes from formalizer:
- The request says to assume no negative numbers; this is represented as a precondition that every input element is non-negative.
- The phrase “more than 1 duplicate of the same number” is interpreted using the examples: exactly two occurrences of a value are allowed, but three or more occurrences are not.
- Because the sequence must be sorted for the result to be true, checking for three equal adjacent elements is equivalent to checking that no value occurs more than twice in any true case.
