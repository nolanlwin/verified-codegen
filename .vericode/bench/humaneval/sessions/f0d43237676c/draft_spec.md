The function takes a class name and a non-empty list of extension names. For each extension, its strength is computed as the number of uppercase English letters minus the number of lowercase English letters in that extension name. The function selects the extension with the greatest strength; if multiple extensions have the same greatest strength, it selects the earliest one in the input list. It returns the class name, followed by a period, followed by the selected extension name.

Notes from formalizer:
- The extension list is specified as non-empty; the original prompt does not define what should happen for an empty list.
- The phrase “fraction CAP - SM” is interpreted as the integer difference CAP - SM.
- Only ASCII English uppercase letters A-Z and lowercase letters a-z are counted. Other characters are ignored for strength computation.
- The method is named Strongest_Extension to match the requested Python-facing name.
