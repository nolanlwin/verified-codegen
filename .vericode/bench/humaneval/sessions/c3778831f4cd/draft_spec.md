The function returns the total number of occurrences of the decimal digit 7 among all nonnegative integers less than the input n that are divisible by 11 or by 13. If n is zero or negative, the result is 0.

Notes from formalizer:
- The phrase “integers less than n” is interpreted in the Python range-style sense: integers i with 0 <= i < n, not all mathematical integers below n.
- The number 0 is considered divisible by 11 and 13, but it contributes 0 occurrences of digit 7, so this does not affect the result.
- Digit counting is over the usual nonnegative decimal representation without leading zeros.
