The function takes a non-empty list of integers and returns the greatest integer contained in that list. For a one-element list, it returns that element. For a longer list, it compares the first element with the maximum of the remaining elements and returns the larger value.

Notes from formalizer:
- The behavior for an empty list is not specified by the request. This specification requires the input list to be non-empty.
- The specification is for integer lists, matching the provided examples.
