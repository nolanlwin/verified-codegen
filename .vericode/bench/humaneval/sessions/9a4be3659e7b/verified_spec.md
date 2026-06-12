The function takes a sequence of non-negative integers representing tree-branch node values. It returns an empty list if the input is empty or contains no even values. Otherwise, it returns a two-element list containing the smallest even value in the input and the index of its first occurrence. If multiple nodes have the same smallest even value, the one with the smallest index is chosen.

Notes from formalizer:
- The stated constraints say the length is at least 1, but the examples and behavior explicitly allow an empty input; this specification allows empty input and returns an empty list for it.
- The input is specified with a precondition that all node values are non-negative.
- The return value is either [] or [smallest_even_value, first_index].
