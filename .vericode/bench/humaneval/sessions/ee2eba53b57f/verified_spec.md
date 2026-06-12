The function takes three integer side lengths. If the three side lengths satisfy all triangle inequalities, it returns the triangle’s area rounded to the nearest hundredth. The area is specified using Heron’s formula in exact arithmetic. If the side lengths do not form a valid triangle, the function returns -1.0.

Notes from formalizer:
- The specification models side lengths as integers. The original Python signature does not state whether non-integer lengths are allowed.
- Rounding is specified as exact nearest-hundredth rounding using mathematical arithmetic, with half cases rounded upward. Python's built-in floating-point round behavior, especially ties, may differ.
- The returned value is modeled as a real number, so an area such as 6.00 is represented mathematically as 6.0.
