The function takes a sequence of integers and returns how many elements have a signed digit sum greater than zero. For nonnegative numbers, the digit sum is the usual sum of decimal digits. For negative numbers, the first/leading digit is treated as negative while the remaining digits are positive; for example, -123 has digit sum -1 + 2 + 3 = 4. The empty input returns 0.

Notes from formalizer:
- The specification treats 0 as having digit sum 0, so it is not counted.
- For a negative number, only the leading decimal digit is negated, matching the examples and prompt.
