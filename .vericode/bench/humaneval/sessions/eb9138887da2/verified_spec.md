The function takes a sequence of integers and returns a sequence of the same length where each output position contains the maximum value seen in the input from the beginning through that position. For an empty input sequence, it returns an empty sequence. For example, input [1, 2, 3, 2, 3, 4, 2] produces [1, 2, 3, 3, 3, 4, 4].

Notes from formalizer:
- Python List[int] is modeled as a mathematical sequence of integers.
- The method is named rolling_max to match the requested Python-facing name.
- The skeleton intentionally contains no implementation logic; the method body is only an assumption placeholder as requested.
