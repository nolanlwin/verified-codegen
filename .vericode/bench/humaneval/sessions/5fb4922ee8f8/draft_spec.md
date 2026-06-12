The function receives an abstract representation of a dictionary's keys. It returns false for an empty collection of keys. For a nonempty collection, it returns true exactly when every key is a string and either all key strings consist only of lowercase letters or all key strings consist only of uppercase letters. If any key is non-string, or if the string keys are mixed between lowercase and uppercase, the result is false.

Notes from formalizer:
- Dictionary values are ignored; only keys affect the result.
- The specification models input as a sequence of abstract keys, where each key is either a string key or a non-string key marker.
- This specification treats a lowercase key string as nonempty and composed entirely of characters 'a' through 'z', and an uppercase key string as nonempty and composed entirely of characters 'A' through 'Z'. Non-letter characters inside string keys are therefore rejected.
