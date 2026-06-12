The function takes a string and returns a new string where each maximal word segment separated by the literal space character is sorted independently in ascending character-code order. The relative order of words is preserved, and all space characters remain as separators, including leading, trailing, and consecutive spaces. Sorting is case-sensitive and includes punctuation or digits as ordinary characters within a word.

Notes from formalizer:
- The separator is specified as the literal space character only; tabs, newlines, and other whitespace are treated as normal word characters.
- The ordering is by character code, which matches ASCII ordering for ASCII inputs.
- The method is named `anti_shuffle` to match the requested compiled Python entry point.
- The skeleton intentionally contains no implementation body beyond the required placeholder.
