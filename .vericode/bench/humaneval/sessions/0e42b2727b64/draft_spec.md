The method takes an encoded string and decodes it group by group. The string is partitioned from left to right into consecutive groups of three characters, with a possible final group of one or two characters. For each complete three-character group, decoding rotates the group one position to the right: the third character becomes first, followed by the original first and second characters. Any final group with fewer than three characters is left unchanged. The returned string is the concatenation of all decoded groups.

Notes from formalizer:
- This specifies the inverse behavior of the provided encoder for complete groups of length three: since encoding maps abc to bca, decoding maps bca back to abc.
- The provided natural language request does not include an explicit Python implementation for decode_cyclic, so the behavior is inferred from encode_cyclic and its docstring.
- If decode_cyclic is called on a string that was not produced by encode_cyclic, the same groupwise right-rotation rule is still specified.
