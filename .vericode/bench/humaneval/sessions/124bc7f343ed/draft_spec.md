The function returns the canonical non-negative greatest common divisor of the two input integers. Negative inputs are treated by taking their absolute values before computing the divisor. If the second normalized input is zero, the result is the first normalized input; otherwise the result follows the standard Euclidean recurrence using the remainder. For inputs 3 and 5 the result is 1, and for inputs 25 and 15 the result is 5.

Notes from formalizer:
- The phrase “a greatest common divisor” can mathematically allow either sign for nonzero inputs; this specification chooses the conventional canonical non-negative result.
- The case where both inputs are zero is not specified in the prompt; this specification defines greatest_common_divisor(0, 0) as 0.
- The method name is kept as greatest_common_divisor to match the requested compiled Python entry point.
