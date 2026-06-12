The function takes a non-empty integer sequence and an integer k within the sequence length. It returns the sum of exactly those values among the first k elements whose absolute value is at most 99, treating those as the elements with at most two digits.

Notes from formalizer:
- The phrase "at most two digits" is interpreted as including negative integers from -99 through 99, based on digit count ignoring the minus sign.
- The input constraints are specified as preconditions: sequence length is between 1 and 100 inclusive, and k is between 1 and the sequence length inclusive.
- The specification sums only the first k elements; elements after position k are ignored.
