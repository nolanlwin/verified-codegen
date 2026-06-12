The function accepts a non-negative real-valued number and returns its fractional, or decimal, part. Semantically, it repeatedly removes whole units of 1 from the input until the remaining value is less than 1; that remaining value is the result. For example, 3.5 produces 0.5, 2.0 produces 0.0, and 0.75 produces 0.75.

Notes from formalizer:
- The original request says "positive" floating point number; the specification allows zero as well, since the fractional part of 0 is naturally 0.
- The phrase "largest integer smaller than given number" is ambiguous for exact integers. This specification follows the usual floor-style interpretation, so an integer input has decimal part 0 rather than 1.
- The formal model uses mathematical real numbers rather than IEEE floating-point rounding behavior.
