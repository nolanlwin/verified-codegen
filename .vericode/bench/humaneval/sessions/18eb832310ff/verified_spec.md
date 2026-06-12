The function takes a list of integers and returns a new list containing exactly the elements from the input that are strictly positive, preserving their original order. Values less than or equal to zero are omitted.

Notes from formalizer:
- The input Python list is modeled as a sequence of integers.
- Positive is interpreted as strictly greater than zero, so zero is excluded, matching the examples.
- The specified method name is `get_positive` to match the expected compiled Python entry point.
