The function takes a list of integers and an integer separator named `delimeter`. It returns a new list with the separator inserted between each pair of consecutive input elements. Empty lists and single-element lists are returned unchanged. For example, `[1, 2, 3]` with separator `4` returns `[1, 4, 2, 4, 3]`.

Notes from formalizer:
- The parameter name is kept as `delimeter` to match the provided Python signature, even though the usual spelling is `delimiter`.
- The specification treats the input as an immutable sequence of integers and defines the returned sequence exactly; it does not specify aliasing or in-place mutation behavior.
- The main method is named `intersperse` in lowercase to match the expected compiled Python entry point.
