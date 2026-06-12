The function takes a non-negative integer n and returns the n-th value of the Fib4 sequence. The base cases are: value 0 at n = 0, value 0 at n = 1, value 2 at n = 2, and value 0 at n = 3. For every n >= 4, the value is the sum of the previous four Fib4 values.

Notes from formalizer:
- The specification restricts inputs to n >= 0; behavior for negative inputs is intentionally unspecified.
- The request asks for an efficient non-recursive implementation, but the provided skeleton contains only the formal behavior contract and an intentionally empty implementation body.
- The method is named fib4 to match the requested Python-facing function name.
