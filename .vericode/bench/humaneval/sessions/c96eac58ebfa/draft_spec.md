The function returns the number of sentences in the input string that start with the word “I”. Sentences are separated by '.', '?', or '!'. Leading spaces and repeated delimiters before a sentence are skipped. A sentence is counted when its first non-space, non-delimiter character begins the word “I”, where “I” is followed by the end of the string, a space, or a sentence delimiter.

Notes from formalizer:
- The repaired skeleton uses character literals for all sentence delimiters, including '!'; this fixes the previous type mismatch between characters and strings.
- The interpretation of the word “I” is conservative: a standalone final “I” and “I” immediately followed by a sentence delimiter are counted, not only occurrences followed by a space.
- Only the method has a postcondition linking the result to the pure specification function.
