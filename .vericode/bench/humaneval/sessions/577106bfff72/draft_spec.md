The function takes two words and returns true exactly when some cyclic rotation of the second word occurs contiguously inside the first word. A rotation includes the original second word unchanged. For example, the second word can be split at any position and the suffix moved before the prefix; if any such rotated form is a substring of the first word, the result is true. The empty second word is treated as a substring and therefore returns true.

Notes from formalizer:
- Rotations are specified to include rotation by zero, meaning the original second word is checked as-is.
- The behavior for an empty second word is not shown in the examples. This specification treats it as true, following the usual convention that the empty string is a substring of every string.
