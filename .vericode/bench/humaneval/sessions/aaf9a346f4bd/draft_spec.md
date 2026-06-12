The function returns the list of all non-empty prefixes of the input text, ordered from shortest to longest. For an empty input string, it returns an empty list. For example, the input "abc" produces ["a", "ab", "abc"].

Notes from formalizer:
- The Python parameter is named `string`, but the specification uses parameter name `s` to avoid confusion with the text type name.
- The return type is modeled as a sequence/list of strings.
- The behavior for the empty string is not shown in the prompt; this specification conservatively defines it as returning an empty list.
