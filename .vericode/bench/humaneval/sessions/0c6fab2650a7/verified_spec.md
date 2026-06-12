The function accepts a nonempty list of strings and returns the string with the largest number of distinct characters. If two or more strings have the same maximum distinct-character count, it returns the lexicographically smallest of those strings. Distinct-character counting treats repeated occurrences within a word as one character.

Notes from formalizer:
- Empty input behavior is not specified in the request, so the specification requires the input list to be nonempty.
- The request says the list contains different words; this specification does not require uniqueness because duplicates do not change the returned string value under the stated selection rule.
- Lexicographical order is formalized using character code order.
- The third example appears to contain an extra quote: `""aaaaaaa`; it is interpreted as returning `"aaaaaaa"`.
