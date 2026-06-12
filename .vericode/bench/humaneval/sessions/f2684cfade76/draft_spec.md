The function returns the number of positions at which the given substring occurs in the input string, counting overlapping occurrences. For each position in the original string, it checks whether the substring begins there and adds one if it does. If the substring is longer than the remaining suffix, no further matches are counted. The empty substring is treated as occurring at every boundary position, so it occurs length + 1 times in a string.

Notes from formalizer:
- The original request does not specify behavior when the substring is empty. This specification chooses the conventional Python slice/loop behavior: an empty substring occurs at every boundary, yielding |string| + 1.
- Overlapping matches are explicitly counted, e.g. "aaaa" with "aa" returns 3.
