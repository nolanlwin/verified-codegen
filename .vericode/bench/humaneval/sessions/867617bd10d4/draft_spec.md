The function takes an integer and returns a pair of integers. The first value is the number of even decimal digits in the input, and the second value is the number of odd decimal digits. For negative inputs, the minus sign is ignored and the digits of the absolute value are counted. The number 0 is treated as having one digit, which is even, so its result is (1, 0).

Notes from formalizer:
- The original examples imply that negative numbers should be handled by counting digits of the absolute value; this specification follows that interpretation.
- The behavior for input 0 was not explicitly stated. This specification treats 0 as a single even digit, returning (1, 0).
- The method is named `even_odd_count` to match the requested Python-facing function name.
