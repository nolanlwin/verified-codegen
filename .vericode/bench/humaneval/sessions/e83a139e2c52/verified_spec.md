The function takes a list of integers and returns a pair of optional integer values. The first component is the largest integer in the list that is strictly negative. The second component is the smallest integer in the list that is strictly positive. If no strictly negative integer exists, the first component has no value. If no strictly positive integer exists, the second component has no value. Zero is ignored for both components.

Notes from formalizer:
- Python None is represented in the formal skeleton by the option-like value NoneInt; present integers are represented as SomeInt(value).
- The requested exported method name is kept as largest_smallest_integers to match the Python test name.
- The specification treats only strictly negative values as candidates for the first result and strictly positive values as candidates for the second result; zeros do not affect either result.
