The function returns true exactly when the input string is nonempty, its final character is an alphabetical letter, and that final letter is not attached to a preceding word character. Concretely, the final character must be an ASCII letter, and it must either be the only character in the string or be immediately preceded by a space. It returns false for the empty string, for strings ending in a non-letter such as a space, and for strings whose final letter is immediately preceded by a non-space character.

Notes from formalizer:
- Alphabetical characters are specified as ASCII letters A-Z and a-z. Python's isalpha() also accepts many Unicode letters, which is broader than this specification.
- The phrase "not a part of a word" is interpreted as: the final letter is isolated from the preceding token by a space, or it is the only character in the string.
- Only the space character ' ' is treated as a word separator, matching the prompt's statement that words are separated by space. Other whitespace such as tabs or newlines is not treated as a separator.
