Given a positive integer, compute the product of its odd decimal digits. If the number contains no odd digits, the result is 0. For example, 1 produces 1, 4 produces 0, and 235 produces 15.

Notes from formalizer:
- The input domain is restricted to positive integers, matching the request. Behavior for zero or negative inputs is unspecified.
- The method is named `digits` so compiled Python can expose the expected lowercase function name.
