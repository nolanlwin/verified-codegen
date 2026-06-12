The function takes two integer sequences of equal length: the actual game scores and the guessed scores. It returns a new integer sequence of the same length where each element is the absolute difference between the corresponding score and guess. Correct guesses therefore produce 0 at that position.

Notes from formalizer:
- The input sequences are specified to have equal length; this is modeled as a required precondition.
- The “guessed correctly” case does not need separate handling because the absolute difference is 0 when the score and guess are equal.
- The method name is lowercase `compare` to match the requested compiled Python entry point.
