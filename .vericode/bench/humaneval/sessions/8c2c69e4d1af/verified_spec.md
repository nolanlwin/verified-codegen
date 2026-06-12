The function returns true exactly when the input string has length at least 3 and, for every consecutive block of three characters, all three characters in that block are pairwise distinct. It returns false for strings shorter than 3 or for any string containing a length-3 consecutive block with a repeated character.

Notes from formalizer:
- Interpreted “every 3 consecutive letters are distinct” as pairwise distinct within each length-3 sliding window.
- The method is named `is_happy` to match the requested Python-facing test name.
