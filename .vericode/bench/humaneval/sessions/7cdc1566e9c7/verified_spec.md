The function returns "Yes" exactly when the input file name satisfies all of these conditions: it contains at most three digit characters total, it contains exactly one dot, the part before the dot is nonempty, the first character of the name is a Latin letter A-Z or a-z, and the part after the dot is exactly one of "txt", "exe", or "dll". In every other case, it returns "No".

Notes from formalizer:
- Digit counting is interpreted as applying to the entire file name string, including both the base name and extension.
- Allowed extensions are treated as case-sensitive and must be exactly lowercase: txt, exe, or dll.
- The specification requires exactly one dot anywhere in the file name, so names with additional dots are invalid even if the final extension is allowed.
- The method is named file_name_check to match the requested compiled Python entry point.
