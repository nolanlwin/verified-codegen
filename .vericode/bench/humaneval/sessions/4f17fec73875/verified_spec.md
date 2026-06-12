The function takes a list of strings and a substring, and returns a new list containing exactly those input strings that contain the substring. The relative order of retained strings is the same as in the input list. If the input list is empty, the result is empty. An empty substring is considered to be contained in every string, matching Python behavior.

Notes from formalizer:
- The specification uses sequences of strings to model the input and output lists.
- Substring containment is specified by character-by-character matching at some position in the string.
- The empty substring case is treated as matching every string, consistent with Python's substring semantics.
