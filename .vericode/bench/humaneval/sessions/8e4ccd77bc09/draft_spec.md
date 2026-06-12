The function takes a sequence of integers, ignores all non-prime values, finds the largest prime value present, and returns the sum of the decimal digits of that largest prime. Primality is defined in the standard way: an integer is prime only if it is at least 2 and has no divisor other than 1 and itself. If there is no prime value in the input, the specified return value is 0.

Notes from formalizer:
- The original examples do not cover the case where the input contains no prime numbers; this specification conservatively chooses 0 for that case.
- Negative integers, 0, and 1 are treated as non-prime and ignored.
- Duplicate prime values do not affect the result except that the largest prime value is still selected.
- The method is named `skjkasdkd` to match the requested compiled Python entry point.
