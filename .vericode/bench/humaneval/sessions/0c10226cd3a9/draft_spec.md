The function takes a sequence of integers and returns the sum of the squares of all elements that are non-negative and odd. Negative values are ignored. Even values, including zero, contribute nothing. If the input sequence is empty, the result is zero.

Notes from formalizer:
- The original Python description mentions ignoring values that are not integers, but this specification uses a statically typed integer sequence, so non-integer elements cannot occur.
- The examples treat zero as contributing zero; in this specification zero is ignored because it is not odd, which yields the same result.
