The function accepts a nonnegative integer n and returns a single string containing the decimal representations of every integer from 0 through n inclusive, in increasing order, separated by exactly one space. For example, input 0 returns "0", and input 5 returns "0 1 2 3 4 5".

Notes from formalizer:
- The original Python type annotation does not state behavior for negative n. This specification conservatively requires n to be nonnegative.
- The output uses ordinary base-10 decimal notation without leading zeros, except for the number 0 itself.
- The main method is named `string_sequence` to match the requested compiled Python entry point.
