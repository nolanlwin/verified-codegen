The function takes a string and returns the number of characters that are uppercase vowels among the characters at even, 0-based indices. The uppercase vowels counted are exactly A, E, I, O, and U. Characters at odd indices are ignored, as are lowercase vowels and all consonants.

Notes from formalizer:
- Even indices are interpreted as 0-based positions: 0, 2, 4, and so on.
- Only the uppercase English vowels A, E, I, O, and U are counted.
- The repaired skeleton uses character literals consistently for vowel comparisons.
