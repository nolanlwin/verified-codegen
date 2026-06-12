The function takes two strings of equal length, each containing only the characters '0' and '1'. It returns a new string of the same length where each character is the binary XOR of the corresponding input characters: the result character is '0' when the two input characters are the same, and '1' when they differ.

Notes from formalizer:
- The specification requires the two input strings to have equal length. The prompt implies binary XOR over two inputs, but does not explicitly state behavior for unequal lengths.
- The specification requires both inputs to contain only '0' and '1', matching the stated precondition in the docstring.
- The exported method is named string_xor to match the requested compiled Python entry point.
