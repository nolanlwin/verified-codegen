The function takes a ragged two-dimensional integer collection and an integer target. It returns all zero-based coordinate pairs where the target occurs. Rows are processed in ascending row-index order. Within each row, matching columns are listed in descending column-index order. Empty input and empty rows produce no coordinates for those positions.

Notes from formalizer:
- The specification uses exact integer equality for matching the target value.
- The returned coordinate pairs are ordered first by increasing row index, and for matches in the same row by decreasing column index.
- No preconditions are imposed; empty outer collections and empty inner rows are valid inputs.
