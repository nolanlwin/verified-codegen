The function takes a list of integers and returns true exactly when the entire list is monotonic: either every adjacent pair is in nondecreasing order, or every adjacent pair is in nonincreasing order. Empty lists and single-element lists are considered monotonic.

Notes from formalizer:
- Interpreted “monotonically increasing or decreasing” as allowing equal adjacent elements, i.e. nondecreasing or nonincreasing, which is the common convention for this problem.
- The specification models the Python list as a sequence of integers.
- The method name is lowercase `monotonic` to match the requested Python-facing name.
