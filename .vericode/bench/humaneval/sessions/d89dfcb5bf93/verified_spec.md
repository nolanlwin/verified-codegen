The function accepts a non-empty sequence of integers and returns its median as a real number. The median is defined by sorting the input values in ascending order, then repeatedly discarding the smallest and largest remaining values until one or two values remain. If one value remains, that value is the median. If two values remain, the median is the arithmetic average of those two values.

Notes from formalizer:
- The specification assumes the input contains integers only; Python lists containing floats, strings, or mixed comparable types are not covered.
- The empty-list case is excluded by a precondition, since the original request does not define what median([]) should return.
- The result type is uniformly real-valued. This matches the even-length example returning 15.0, but differs from Python’s usual dynamic behavior where an odd-length integer input might return an int such as 3 rather than 3.0.
- The method is named `median` to match the requested compiled Python entry point.
