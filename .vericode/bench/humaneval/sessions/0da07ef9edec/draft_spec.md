The function returns true exactly when x is an integer power of n using a nonnegative integer exponent. Exponent 0 is allowed, so any base raised to 0 gives 1, making x = 1 a simple power. The examples are covered: 1 is a power of 4, 2 and 8 are powers of 2, while 3 is not a power of 2 or 1, and 5 is not a power of 3.

Notes from formalizer:
- The phrase “n**int = x” is interpreted as “there exists a nonnegative integer exponent k such that n^k equals x.” Negative exponents are not modeled because they generally produce fractions rather than integers.
- This specification treats exponent 0 as valid for every integer base, including 0, so 0^0 is modeled as 1.
- The specification is total over integer inputs, including negative bases and negative x values.
