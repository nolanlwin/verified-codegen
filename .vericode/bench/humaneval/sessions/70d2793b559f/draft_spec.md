For any input integer greater than 1, the function returns the prime factorization of that integer as a list of integers. Factors appear from smallest to largest, and repeated prime factors appear once for each occurrence in the factorization. The product of the returned factors is intended to equal the input.

Notes from formalizer:
- The request does not define behavior for n <= 1, so the method is specified only for n > 1.
- The formal return type is an immutable sequence of integers, corresponding to the requested Python list of integers.
- The specification defines factorization by trial division starting at 2, which fixes the intended ordering and multiplicity of factors.
