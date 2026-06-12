For an input list of strings, the result is the first string whose length is maximal among all strings in the list. If the input list is empty, the result is no string / None. When multiple strings share the maximum length, the earliest one in the input order is selected.

Notes from formalizer:
- The optional return is modeled explicitly as either NoneString for an empty input or SomeString(value) for a present string.
- The method is named longest to match the requested compiled entry point.
- The input list is represented as a sequence of strings in the specification.
