The function accepts a music string made from space-separated note tokens. Valid tokens are `o` for a whole note worth 4 beats, `o|` for a half note worth 2 beats, and `.|` for a quarter note worth 1 beat. Spaces may appear between notes, and leading, trailing, or repeated spaces are permitted. The result is the sequence of beat lengths obtained by scanning the input from left to right and translating each recognized note token into its corresponding integer value.

Notes from formalizer:
- The repair changes space comparisons to use character literals, matching the type of indexed string characters.
- Inputs are constrained to valid music strings containing only the supported note forms and spaces in positions allowed by the validity predicate.
- The specification treats any standalone `o` not immediately followed by `|` as a whole note, provided it is followed by a space or the end of the string.
