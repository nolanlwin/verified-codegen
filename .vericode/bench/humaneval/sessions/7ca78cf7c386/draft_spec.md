The function returns true exactly when each distinct character appearing in the first string also appears somewhere in the second string, and each distinct character appearing in the second string also appears somewhere in the first string. Character order and the number of times each character occurs are ignored.

Notes from formalizer:
- The examples indicate set equality of characters, not multiset equality; duplicate counts are ignored.
- The specification is case-sensitive and treats every character in the input strings as significant, not only alphabetic letters.
- The empty-string behavior follows the same rule: two empty strings have the same character set, while an empty string and a non-empty string do not.
