The function takes a string and returns the number of vowels in it. The regular vowels counted are a, e, i, o, and u, in either lowercase or uppercase. The letter y, also in either lowercase or uppercase, is counted as a vowel only when it appears as the final character of the input string. All other characters contribute zero to the count.

Notes from formalizer:
- Repaired the character comparisons so uppercase vowels and uppercase Y are compared as characters rather than strings.
- The specification treats uppercase vowels as vowels, matching the provided example "ACEDY" -> 3.
- For the empty string, the count is 0; y/Y is counted only if it is the last character and the string is nonempty.
