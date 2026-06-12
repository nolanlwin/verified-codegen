The function returns true exactly when the input string reads the same forwards and backwards. Empty strings and one-character strings are palindromes. For longer strings, the first and last characters must match, and the middle substring must also be a palindrome.

Notes from formalizer:
- The comparison is exact and case-sensitive.
- Spaces, punctuation, and all other characters are treated as ordinary characters; no normalization is performed.
- The exported method is named `is_palindrome` to match the requested Python test name.
