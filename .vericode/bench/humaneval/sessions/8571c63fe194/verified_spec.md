The function returns a new sequence containing the input integers sorted in ascending order by their point value. The point value is the sum of decimal digits for nonnegative integers. For negative integers, the leading digit contributes negatively and the remaining digits contribute positively, so -12 has point value -1 + 2 = 1. If two numbers have the same point value, their relative order from the original input is preserved. The empty input returns the empty output.

Notes from formalizer:
- The treatment of negative integers is ambiguous in the natural-language phrase “sum of their digits.” This specification uses the interpretation that matches the provided example: the sign applies to the most significant digit only, e.g. -1 has point value -1, -11 has point value 0, and -12 has point value 1.
- Tie-breaking by original index is modeled as a stable sort: equal point values remain in their original relative order.
- The main method is named order_by_points as requested.
