The function takes a string containing space-separated lowercase letters and returns a dictionary whose keys are the letters that occur most frequently and whose values are their occurrence counts. Spaces are ignored. If multiple letters tie for the maximum frequency, all tied letters are included. If the input contains no letters, the result is an empty dictionary.

Notes from formalizer:
- The specification treats each non-space character as an individual one-character key; it does not validate that the input is lowercase or that letters are separated by exactly one space.
- Dictionary ordering is not specified or relevant.
- The result type is modeled as a map from one-character strings to integer counts, matching the Python-style dictionary intent more closely than using character keys.
