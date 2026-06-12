Given an input string, produce a string of the same length by processing characters from left to right. Each lowercase English letter `a` through `z` is replaced by the corresponding uppercase letter, and each uppercase English letter `A` through `Z` is replaced by the corresponding lowercase letter. All other characters are left unchanged.

Notes from formalizer:
- The fixed skeleton uses character literals for all single-character mappings, including `'z'`, avoiding the previous type mismatch caused by using a string literal in a character-returning function.
- The specification is conservative: it flips only ASCII English letters A-Z and a-z. Non-ASCII letters and all non-letter characters are unchanged.
- All postconditions are on the method only; the semantic functions have no postconditions.
