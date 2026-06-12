The function takes a non-empty list of integers and returns the sum of all values that are even and located at odd indices. Indices are interpreted using the usual Python convention, starting at 0, so the relevant positions are 1, 3, 5, and so on. If no qualifying elements exist, the result is 0.

Notes from formalizer:
- The input is required to be non-empty, matching the problem statement, although the same summation rule would also be meaningful for an empty list.
- “Odd indices” is interpreted as 0-based indexing, consistent with Python lists; for example, in [4, 2, 6, 7], only index 1 contributes, giving 2.
- Evenness is tested by divisibility by 2, so negative even integers also qualify.
