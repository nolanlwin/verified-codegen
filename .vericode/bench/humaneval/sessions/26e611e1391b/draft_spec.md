For a positive integer n, the function returns the number of n-digit positive integers whose first digit is 1 or whose last digit is 1. For n = 1, only the number 1 qualifies, so the result is 1. For n = 2, there are 18 qualifying numbers. For each additional digit length beyond 2, the count is multiplied by 10.

Notes from formalizer:
- The input is specified as a positive integer, so n must be greater than 0.
- The method is named starts_one_ends to match the expected compiled Python entry point.
- The specification uses the recurrence: result(1) = 1, result(2) = 18, and result(n) = 10 * result(n - 1) for n > 2.
