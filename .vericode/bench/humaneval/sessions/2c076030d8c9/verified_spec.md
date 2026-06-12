The function takes a sequence of integers and returns a sequence of the same length. Positions with odd zero-based indices keep exactly the same values as in the input. Values from positions with even zero-based indices are collected, sorted in ascending nondecreasing order, and placed back into the even-indexed positions from left to right.

Notes from formalizer:
- The Python list is modeled as a sequence of integers; behavior for non-integer elements is not specified here.
- Indices are interpreted as zero-based, matching the examples.
- Sorting is ascending and nondecreasing, so duplicate even-indexed values are preserved but their relative identity is not distinguished.
