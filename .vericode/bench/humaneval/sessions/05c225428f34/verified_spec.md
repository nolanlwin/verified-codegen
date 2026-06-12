The function takes a list of strings and a prefix string, and returns a new list containing exactly those input strings that start with the given prefix. The relative order of retained strings is preserved. If the input list is empty, the result is empty. If the prefix is longer than a candidate string, that string is not included. An empty prefix matches every string.

Notes from formalizer:
- The specification models Python lists as immutable sequences of strings.
- The required exported method name is written as filter_by_prefix to match the requested Python test name.
- No implementation is provided in the method body; it is intentionally left as an assumed placeholder for verified code generation.
