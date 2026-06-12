The function takes a sequence of integers and returns the largest zero-based index i such that i has a preceding element and arr[i] is strictly less than arr[i - 1]. If the sequence is empty, has one element, or has no such descending adjacent pair, it returns -1.

Notes from formalizer:
- The phrase “not greater than or equal to the element immediately preceding it” is formalized as strictly less than the preceding element.
- The stated assumption that the input contains no duplicate values is not required for this behavior, so the specification does not impose it as a precondition.
- Indices are interpreted using Python-style zero-based indexing, matching the examples.
