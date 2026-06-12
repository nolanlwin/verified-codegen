The function takes a sequence of abstract Python-like values and returns a sequence containing exactly the integer values from the input, in their original order. Non-integer values are omitted. For example, an input representing ['a', 3.14, 5] would produce [5], and an input representing [1, 2, 3, 'abc', {}, []] would produce [1, 2, 3].

Notes from formalizer:
- Dafny does not directly model Python's arbitrary List[Any], so the specification uses an abstract value type with two cases: integer values and all other values.
- The treatment of Python bool values is ambiguous because bool is a subclass of int in Python. This specification treats only explicit integer-tagged values as integers; all other values are filtered out.
- The requested compiled Python entry point name is preserved by naming the method filter_integers.
