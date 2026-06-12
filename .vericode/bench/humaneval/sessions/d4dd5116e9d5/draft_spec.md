The function takes a non-empty sequence of integers and returns the smallest possible sum of any contiguous, non-empty sub-array. A sub-array may have length 1 up to the full length of the input. For example, for [2, 3, 4, 1, 2, 4], the result is 1, and for [-1, -2, -3], the result is -6.

Notes from formalizer:
- The input is specified as non-empty because the requested minimum over non-empty sub-arrays is undefined for an empty array.
- The method name is exactly minSubArraySum to match the requested compiled Python entry point.
- The specification uses mathematical integer arithmetic, so there is no overflow behavior.
