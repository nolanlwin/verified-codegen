The function takes a text string and returns a list of parenthesis-group strings. Spaces are ignored. As the input is scanned from left to right, each top-level balanced parenthesis group is collected as one output string, preserving its internal nested parentheses. For example, the input `( ) (( )) (( )( ))` produces `['()', '(())', '(()())']`.

Notes from formalizer:
- The specification treats the result as a sequence/list of strings.
- The intended problem statement appears to assume inputs consist of balanced parenthesis groups possibly separated by spaces.
- For robustness, the skeleton gives a defined behavior for other characters by ignoring them, and unmatched closing parentheses are ignored. Incomplete trailing open groups are not emitted. These edge cases are ambiguous in the original request and are not expected for valid benchmark inputs.
- The method name is `separate_paren_groups` to match the requested compiled Python entry point.
