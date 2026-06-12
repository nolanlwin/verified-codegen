The function takes a list of integers and an integer threshold. It returns true exactly when every element in the list is strictly less than the threshold. The empty list satisfies this condition and returns true.

Notes from formalizer:
- The phrase "below threshold" is interpreted as strictly less than the threshold, not less than or equal to it.
- The input list is modeled as a sequence of integers.
