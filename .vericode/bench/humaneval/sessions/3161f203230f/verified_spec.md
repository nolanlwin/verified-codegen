The function takes a sequence of integers and returns true exactly when there exist two different positions in the sequence whose values add up to zero. A single zero does not count as a pair, but two zeroes at distinct positions do. If no such distinct pair exists, the function returns false.

Notes from formalizer:
- The input is modeled as a sequence of integers rather than a mutable array, matching the list-like behavior needed for the specification.
- Distinct elements are interpreted as elements at distinct indices, not necessarily distinct numeric values; therefore [0, 0] should return true.
- The method name is kept as pairs_sum_to_zero to match the expected compiled Python test name.
