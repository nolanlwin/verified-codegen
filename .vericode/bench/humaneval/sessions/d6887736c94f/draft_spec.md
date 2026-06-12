The function takes an input string and returns a new string with all vowels removed. The vowels removed are lowercase and uppercase A, E, I, O, and U. All other characters, including consonants, whitespace, newlines, punctuation, and other symbols, are preserved in their original order.

Notes from formalizer:
- Fixed the character literal for uppercase U so it is compared as a character, not as a string.
- The specification treats only A, E, I, O, U and their lowercase forms as vowels; for example, 'y' is not removed.
- The method body remains a placeholder as required.
