The function returns whether the input integer can be expressed as the sum of exactly four positive even integers. Since the smallest such sum is 2 + 2 + 2 + 2 = 8, the result is true exactly for even integers greater than or equal to 8, and false otherwise.

Notes from formalizer:
- The method is named exactly `is_equal_to_sum_even` to match the requested compiled Python entry point.
- Negative integers, odd integers, and integers less than 8 are specified to return false.
- The recursive specification subtracts 2 until reaching 8 or falling below 8, which captures the required parity and minimum-sum conditions.
