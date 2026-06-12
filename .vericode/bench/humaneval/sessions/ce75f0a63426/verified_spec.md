Given a string and a nonnegative integer n, the function scans the string from left to right, treating spaces as word separators. It returns all nonempty words whose number of consonants is exactly n, preserving their original order. Vowels are a, e, i, o, u in either lowercase or uppercase; all other letters, including y, are counted as consonants. An empty input string, or an input containing no matching words, produces an empty result list.

Notes from formalizer:
- The request says the input contains only letters and spaces. The formal skeleton requires only that n is nonnegative; if other characters appear, the spec treats any non-space non-vowel character as a consonant.
- Consecutive spaces and leading/trailing spaces are treated as separators and do not produce empty words.
- The return value is modeled as a sequence of strings, corresponding to a Python list of strings.
