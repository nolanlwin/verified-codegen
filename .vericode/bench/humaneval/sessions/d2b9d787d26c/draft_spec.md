The function takes a nonnegative integer exponent n and a positive integer modulus p, and returns 2 raised to the power n modulo p. For n = 0, the result is 1 modulo p.

Notes from formalizer:
- The request does not define behavior for negative exponents, so the specification excludes n < 0.
- The request does not define behavior for zero or negative moduli, so the specification requires p > 0.
- For p = 1, the specified result is 0 for all n, including n = 0, because 1 modulo 1 is 0.
