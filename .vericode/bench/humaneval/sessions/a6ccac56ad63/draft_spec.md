The function takes a list of positive integers and returns all input elements whose decimal digits are all odd. Any number containing at least one even digit, including 0, 2, 4, 6, or 8, is excluded. The returned list is sorted in increasing numeric order.

Notes from formalizer:
- The input is specified as positive integers only; behavior for zero or negative integers is left outside the specification.
- The phrase “all elements” is interpreted as preserving duplicate qualifying values, then sorting them in nondecreasing order.
- The name unique_digits is interpreted as referring to digits being odd-only, not to removing duplicate elements.
