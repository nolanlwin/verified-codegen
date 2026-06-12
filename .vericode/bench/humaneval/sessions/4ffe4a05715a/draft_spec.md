The function returns true exactly when the input integer is prime. Integers less than or equal to 1 are not prime. For integers 2 or greater, the result is true if and only if no integer divisor from 2 up to one less than the input divides it evenly; otherwise the result is false.

Notes from formalizer:
- The specification accepts all integers, including negative values; all integers less than or equal to 1 are specified as non-prime.
- The divisor search is specified naively from 2 through n - 1, matching the mathematical definition rather than optimizing up to the square root.
- The method is named `is_prime` to match the requested compiled Python entry point.
