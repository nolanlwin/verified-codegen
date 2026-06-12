The function takes two integers and returns the product of their unit digits. For negative inputs, the unit digit is interpreted by ignoring the sign, so the unit digit of -15 is 5. For example, 148 and 412 produce 8 * 2 = 16, and 14 and -15 produce 4 * 5 = 20.

Notes from formalizer:
- The request says the input is always valid; since all integers are valid for this operation, no additional preconditions are imposed.
- For negative integers, the specification follows the provided example and treats the unit digit as the last digit of the absolute value.
