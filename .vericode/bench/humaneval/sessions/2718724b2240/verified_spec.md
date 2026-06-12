The function accepts two positive integers. If the first integer is greater than the second, it produces the integer result -1. Otherwise, it sums all integers in the inclusive range from n through m, divides by the number of terms to get the average, rounds that average to the nearest integer using half-to-even tie breaking, and returns the rounded value formatted as a binary string with the prefix "0b".

Notes from formalizer:
- The requested behavior has mixed return types: integer -1 for the invalid range and a binary string for the valid range. The specification models this with a tagged result: IntResult(-1) or StringResult(...).
- The phrase “round to the nearest integer” is ambiguous for exact halves. The example rounded_avg(20, 33) => "0b11010" indicates half-to-even rounding, matching Python's round behavior, because the exact average is 26.5 and the result is 26 rather than 27.
- The request states that n and m are positive integers, so the method requires both inputs to be greater than zero.
- The main method is named rounded_avg as requested for Python-facing naming.
