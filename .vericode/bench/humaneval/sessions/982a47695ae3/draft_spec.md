The function takes a non-empty sequence of positive integers. It returns the largest positive integer whose number of occurrences in the input is at least as large as the integer itself. If no positive integer satisfies that frequency condition, it returns -1.

Notes from formalizer:
- The input preconditions enforce the request's assumption that the list is non-empty and contains only positive integers.
- The specification treats frequency as the number of exact integer matches in the original input sequence.
- The method is named `search` in lowercase to match the requested exported/tested name.
