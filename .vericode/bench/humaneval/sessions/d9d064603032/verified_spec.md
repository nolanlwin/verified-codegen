The function takes two non-empty integer lists and returns "YES" if it is possible, by exchanging any number of elements between the two lists, to make every element of the first list even. Otherwise, it returns "NO".

Because exchanges preserve the length of the first list, this is possible exactly when the total number of even elements across both input lists is at least the length of the first list.

Notes from formalizer:
- The specification assumes an exchange can swap arbitrary elements between the two lists any number of times, so only the total availability of even numbers matters.
- The method is named `exchange` to match the requested Python-facing function name.
- Inputs are required to be non-empty, matching the problem statement.
