The function takes an input string and returns the sequence of non-empty words obtained by scanning left to right. A comma or a space ends the current word. Consecutive separators, leading separators, and trailing separators do not produce empty words. All other characters are included in words unchanged and in their original order.

Notes from formalizer:
- Delimiters are specified as exactly the comma character ',' and the ordinary space character ' '. Other whitespace such as tabs or newlines is treated as part of a word.
- The return value is modeled as a sequence of strings rather than a mutable array; it represents the same ordered list of words expected by the Python behavior.
- The method name is kept as words_string to match the requested Python-facing name.
