The function takes an encoded lowercase string and returns a decoded string of the same length. Each character is shifted backward by 5 positions in the lowercase English alphabet, wrapping around at the beginning: for example, 'f' decodes to 'a', 'a' decodes to 'v', and 'e' decodes to 'z'. The input is required to contain only lowercase letters 'a' through 'z'.

Notes from formalizer:
- The original encoder maps every input character into a lowercase letter using arithmetic on character codes. Because that mapping is many-to-one for arbitrary non-lowercase source characters, the decoder can only recover the canonical lowercase character obtained by shifting backward by 5, not the exact original arbitrary character.
- The specification requires the encoded input to consist only of lowercase English letters, matching the documented expectation that the input was produced by the encoder.
- The exported method is named `decode_shift` to match the requested Python test name.
