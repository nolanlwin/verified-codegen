Given an input sentence, the function scans its words in their original order and returns a string containing exactly those words whose lengths are prime numbers. The selected words are separated by a single space in the output, with no leading or trailing space. Word lengths 2, 3, 5, 7, etc. are considered prime; lengths 0 and 1 are not prime.

Notes from formalizer:
- The prompt's constraints say the sentence contains only letters, but the examples and description require spaces between words. This specification treats spaces as word separators and all other characters as part of words.
- Multiple consecutive spaces, leading spaces, or trailing spaces are handled conservatively by ignoring empty words and producing normalized single-space separation between selected words.
- The specification method is named exactly `words_in_sentence` for compatibility with the requested compiled Python entry point.
- `WordsInSentenceSpec` is written with accumulator parameters: the input suffix still to scan, the current word being built, and whether a previous selected word has already been emitted. The method calls it with the initial accumulator values.
