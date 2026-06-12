The function takes two integer lists and returns a list containing exactly the values that occur in both inputs. Each common value appears at most once in the output, even if it appears multiple times in either input. The output is sorted in ascending numeric order. If there are no shared values, the result is the empty list.

Notes from formalizer:
- The Python signature uses untyped lists, but the formal specification treats inputs as lists/sequences of integers, matching the examples and numeric sorting behavior.
- Sorting is specified as ascending order according to integer comparison.
- The method body is intentionally empty except for an assumption placeholder; only the required functional contract is specified.
