The function takes a list of strings, removes every string whose length is odd, and returns the remaining strings sorted in ascending order. Sorting is primarily by string length; when two strings have the same length, they are sorted alphabetically in lexicographic order. Duplicate strings are preserved.

Notes from formalizer:
- The prompt says, “You may assume that all words will have the same length,” but the examples contain words of different lengths. The specification follows the main requested behavior: filter out odd-length strings, then sort by length and alphabetically for ties.
- Alphabetical order is interpreted as lexicographic order over character/codepoint ordering.
- The method is named `sorted_list_sum` to match the requested compiled Python entry point.
