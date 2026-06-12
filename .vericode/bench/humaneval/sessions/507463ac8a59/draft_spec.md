The function accepts a non-negative integer and returns its standard base-2 representation as a string, wrapped with the literal prefix and suffix "db". For example, 15 produces "db1111db" and 32 produces "db100000db". The value 0 is represented as "db0db". The binary portion contains only '0' and '1' characters and has no leading zeroes except for the representation of zero itself.

Notes from formalizer:
- The original request does not specify behavior for negative inputs; this specification restricts the input to non-negative integers.
- The behavior for input 0 is not shown in the examples; this specification chooses the conventional binary representation "0", yielding "db0db".
- The method name is kept as decimal_to_binary to match the expected compiled Python entry point.
