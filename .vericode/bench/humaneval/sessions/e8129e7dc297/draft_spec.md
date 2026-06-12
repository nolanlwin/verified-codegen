The requested function returns the shortest palindrome that starts with the input string. It does this by identifying the longest suffix of the input that is already a palindrome, then appending the reverse of the prefix that appears before that suffix. For an empty input, the result is the empty string. For example, `cat` becomes `catac`, and `cata` also becomes `catac`.

Notes from formalizer:
- The specification models strings abstractly and recursively: reversing a string, checking whether a string is a palindrome, and finding the prefix before the longest palindromic suffix are all defined as pure semantic functions.
- The method body is intentionally left unimplemented with an assumption placeholder, so this is a verification-oriented specification skeleton rather than executable logic.
- The exposed method is named `make_palindrome` to match the requested compiled Python entry point.
