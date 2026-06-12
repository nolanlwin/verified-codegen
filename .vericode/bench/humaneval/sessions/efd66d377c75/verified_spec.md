The function takes two lists of strings and computes the total number of characters across all strings in each list. It returns the list with the smaller total character count. If both lists have the same total character count, it returns the first input list.

Notes from formalizer:
- The specification treats Python lists of strings as sequences of strings.
- Tie-breaking is specified as returning the first list when the total character counts are equal.
- Character count is based on the length of each string, summed over the whole list.
