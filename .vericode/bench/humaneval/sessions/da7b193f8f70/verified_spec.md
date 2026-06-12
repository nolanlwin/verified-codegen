Given a non-empty sequence of integers, compute the sum of elements whose index is even and whose value is odd. Indexing is interpreted as zero-based, so positions 0, 2, 4, and so on are considered even positions. If no such elements exist, the result is 0.

Notes from formalizer:
- The phrase "even positions" is interpreted using zero-based indexing, consistent with the examples: [5, 8, 7, 1] sums indices 0 and 2 to get 12.
- The input is required to be non-empty, matching the problem statement, although the summation rule would naturally extend to empty sequences with result 0.
- Oddness is specified as value % 2 != 0, which correctly classifies negative odd integers as odd under mathematical integer modulo semantics.
