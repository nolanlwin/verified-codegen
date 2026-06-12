The function takes two closed integer intervals, each represented as a pair of integers `(start, end)`, with the precondition that `start <= end` for each interval. It computes the overlap of the two intervals. If the intervals do not overlap, it returns `"NO"`. Otherwise, it computes the length of the overlap as `overlap_end - overlap_start`. It returns `"YES"` exactly when that length is a prime number, and `"NO"` otherwise.

Notes from formalizer:
- The overlap length is specified as `end - start`, matching the prompt's example where the intersection `(2, 3)` has length `1`; it is not the count of integer points in the intersection.
- Because intervals are closed, intervals that touch at a single endpoint are considered to intersect, but their intersection length is `0`, which is not prime, so the result is `"NO"`.
- Prime means an integer greater than 1 with no divisor from 2 up to one less than itself.
- The method is named `intersection` to match the requested Python-facing function name.
