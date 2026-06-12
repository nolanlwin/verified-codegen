The function takes a string and returns true exactly when the string is a well-balanced parenthesis sequence. It scans the string from left to right, tracking the number of unmatched opening parentheses. An opening parenthesis increases the balance, a closing parenthesis is valid only if there is an unmatched opening parenthesis to match it, and any other character makes the result false. The final result is true only if the scan ends with balance zero.

Notes from formalizer:
- The repaired specification avoids direct character literals by comparing against the first character of one-character string literals, which prevents the reported parse error.
- Although the original prompt states the input is a string of only '(' and ')', the specification conservatively returns false if any other character is encountered.
- All postconditions are placed only on the method, and the method body is exactly assume false.
