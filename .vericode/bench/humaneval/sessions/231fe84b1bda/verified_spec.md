The function returns a new integer list containing exactly those input elements whose total number of occurrences in the original input is one. Elements that appear two or more times anywhere in the input are omitted entirely. The relative order of the retained elements is the same as in the input.

Notes from formalizer:
- The input Python list is modeled as an immutable sequence of integers in the specification.
- The behavior follows the docstring wording: elements occurring more than once are removed completely, not merely deduplicated to a single copy.
