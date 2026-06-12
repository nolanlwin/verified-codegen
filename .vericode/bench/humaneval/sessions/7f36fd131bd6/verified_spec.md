The function accepts a positive integer n and returns the product n! * (n-1)! * ... * 1!. For n = 1, the result is 1. For larger n, the result is n! multiplied by the special factorial of n - 1.

Notes from formalizer:
- The input domain is restricted to n > 0, matching the problem statement.
- The specification uses mathematical integers, so it does not model fixed-width integer overflow.
- The exported method is named special_factorial to match the requested Python-facing name.
