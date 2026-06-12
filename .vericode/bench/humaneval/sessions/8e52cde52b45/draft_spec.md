The function takes an input string and returns the sum of the character codes for exactly those characters that are uppercase English letters from A through Z. Characters outside the range A-Z, including lowercase letters, digits, punctuation, whitespace, and non-English uppercase characters, contribute 0. The empty string returns 0.

Notes from formalizer:
- The original name `digitSum` is potentially misleading because the task sums uppercase-character codes, not digit values.
- The phrase “upper characters” is interpreted as ASCII uppercase letters A through Z only.
- Character codes are interpreted as standard ASCII/Unicode code points for A-Z, so A is 65 through Z is 90.
