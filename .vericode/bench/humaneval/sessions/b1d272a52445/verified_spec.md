For a positive integer n, return a list of exactly n integers. The first element is n. Each subsequent element is 2 greater than the previous element, preserving the parity of n. Thus, if n is odd, the list contains n consecutive odd values starting at n; if n is even, it contains n consecutive even values starting at n.

Notes from formalizer:
- The input is specified as a positive integer, so behavior for n <= 0 is intentionally left unspecified.
- The phrase “next odd/even number” is interpreted as the next larger number with the same parity, i.e. adding 2 at each level.
- The returned Python list is modeled internally as a sequence of integers.
