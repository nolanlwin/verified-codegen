The function takes an integer N between 0 and 10000 inclusive. It computes the sum of the decimal digits of N, then returns the standard base-2 string representation of that digit sum with no leading zeroes, except that the value 0 is represented as "0".

Notes from formalizer:
- The prompt says "sum of its digits in binary," but the examples match summing the decimal digits of N and then converting that sum to binary. For example, 150 has decimal digit sum 6, whose binary representation is "110".
- The prose says N is positive, but the stated constraints allow N = 0. This specification accepts 0 and returns "0".
- The method name is exactly `solve` to match the requested Python entry point.
