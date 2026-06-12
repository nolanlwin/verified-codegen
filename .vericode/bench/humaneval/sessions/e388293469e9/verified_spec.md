The function takes a sequence of integers, ignores every integer outside the inclusive range 1 through 9, orders the remaining digits from largest to smallest, and returns the corresponding English digit names. Duplicate valid digits are preserved. An empty input, or an input with no valid digits, produces an empty output.

Notes from formalizer:
- The specification uses a direct descending sort of valid digits, which is equivalent to sorting ascending and then reversing for the values that are ultimately returned.
- Invalid or “strange” numbers are ignored entirely rather than appearing in any intermediate or final output.
- The method is named `by_length` to match the expected compiled Python entry point.
