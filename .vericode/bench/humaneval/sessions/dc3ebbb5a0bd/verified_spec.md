The function returns the largest even integer in the inclusive range from x to y. It searches downward from y: if y is below x, there is no valid number and the result is -1; if y is even, y is the answer; otherwise, the answer is the same as for the range ending at y - 1.

Notes from formalizer:
- The docstring says the inputs are positive numbers, but the specification is defined for all integers because the described behavior is meaningful for any integer x and y.
- The main method is named choose_num to match the requested compiled Python entry point.
- If x is greater than y, the result is specified as -1, matching the example choose_num(13, 12) = -1.
