The function takes a nonempty integer sequence and an integer k between 0 and the sequence length. It returns the k largest values from the input, preserving duplicate occurrences, sorted in ascending order. If k is 0, the result is the empty list. The documented input bounds are treated as preconditions: the input length is from 1 to 1000, and every element is between -1000 and 1000 inclusive.

Notes from formalizer:
- The request says k is positive, but the note allows 0 <= k <= len(arr); this specification allows k = 0 and returns an empty list in that case.
- “Sorted list” is interpreted as ascending order, matching the examples.
- Duplicates are retained, so if one of the maximum values appears multiple times, multiple copies may appear in the result.
- The method is named `maximum` to match the requested compiled Python entry point.
