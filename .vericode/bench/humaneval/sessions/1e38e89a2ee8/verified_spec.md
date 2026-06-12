The function takes two positive integers and returns the even decimal digits that lie between them inclusively, regardless of input order. The result is ordered ascending. Since the requested values are digits, only positive one-digit even values are included: 2, 4, 6, and 8. Values 10 and above are not included, even if they are even and lie within the numeric range.

Notes from formalizer:
- The input precondition is that both arguments are positive integers, matching the request. Behavior for zero or negative inputs is intentionally unspecified.
- The output is modeled as a sequence of integers corresponding to the Python list result.
- The word “digits” is interpreted literally, so the specification excludes multi-digit even numbers such as 10, 12, and 14.
