The function returns the minimum number of element changes needed to make the input integer sequence read the same forwards and backwards. It compares symmetric pairs from the two ends inward. Each pair that already matches requires no change; each pair that differs requires exactly one change, because either element can be changed to match the other. Empty sequences, single-element sequences, and the unpaired middle element of an odd-length sequence require zero changes.

Notes from formalizer:
- The specification treats the input as a sequence of integers rather than a mutable array.
- For an empty input sequence, the specified result is 0.
- The method is named `smallest_change` to match the requested compiled Python entry point.
