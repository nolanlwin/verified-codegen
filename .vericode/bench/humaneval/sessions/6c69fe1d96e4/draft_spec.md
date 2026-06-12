For an input integer n greater than 1, the function returns the largest positive integer strictly smaller than n that divides n evenly. It searches conceptually downward from n - 1 to 1 and returns the first divisor found. For prime inputs, the result is 1.

Notes from formalizer:
- The specification requires n > 1. The behavior for n <= 1 is not defined because there is no positive divisor strictly smaller than n in the usual sense.
- The exported method is named largest_divisor to match the requested Python test name.
- Only the method has a postcondition tying its result to the pure semantic specification.
