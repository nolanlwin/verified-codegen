The function takes a sequence of integers and computes a transformed sum. For each element, its zero-based index determines how it contributes: if the index is a multiple of 3, the element is squared; otherwise, if the index is a multiple of 4, the element is cubed; otherwise, the element is used unchanged. The function returns the sum of all transformed elements. An empty input returns 0.

Notes from formalizer:
- Indexes are interpreted as zero-based, matching Python list indexing.
- Index 0 is considered a multiple of 3, so the first element is squared.
- If an index is a multiple of both 3 and 4, the multiple-of-3 rule takes precedence, so the element is squared rather than cubed.
