The function takes a sequence of non-negative integers and returns a new sorted sequence without modifying the input. If the input has length 0 or 1, it is returned unchanged. Otherwise, the first and last values are added: when their sum is odd, the result is sorted in ascending order; when their sum is even, the result is sorted in descending order.

Notes from formalizer:
- The previous parse error was caused by using `array` as a parameter name, which conflicts with a reserved built-in type name. The fixed skeleton uses `a` instead.
- Sorting semantics are defined recursively by insertion into an ascending or descending sorted sequence.
- The specification assumes all input elements are non-negative, matching the original request.
