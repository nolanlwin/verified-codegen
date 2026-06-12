The function takes two strings, `s` and `c`. It constructs a new string by scanning `s` from left to right and removing every character that appears anywhere in `c`, preserving the order of all remaining characters. It then checks whether this filtered string is a palindrome, meaning it reads the same forward and backward. The returned value is a pair containing the filtered string and the Boolean palindrome result.

Notes from formalizer:
- Characters in `c` are treated as a membership set for deletion; duplicate characters in `c` have no additional effect.
- The palindrome check is case-sensitive and character-exact.
- The specified method name is `reverse_delete` to match the requested Python-facing name.
