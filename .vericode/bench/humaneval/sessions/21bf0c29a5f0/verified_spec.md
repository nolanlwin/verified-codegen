The requested function takes a text string. If the string is empty, it returns no hash value. Otherwise, it returns the lowercase hexadecimal MD5 digest of the text after encoding it as UTF-8. For example, the input "Hello world" should produce "3e25960a79dbc69b674cd4ec67a72c62".

Notes from formalizer:
- The original Python docstring says the empty string should return None. The formal skeleton represents this with an explicit optional-string result: NoneString for no value, and SomeString(hash) for a present hash.
- The request does not specify the character encoding used before hashing. This specification assumes UTF-8, matching the usual Python pattern hashlib.md5(text.encode('utf-8')).hexdigest().
- The method body is intentionally empty except for the required assumption placeholder; all behavior is captured by the specification.
- The externally tested Python function name is expected to be string_to_md5; the skeleton uses that method name exactly.
