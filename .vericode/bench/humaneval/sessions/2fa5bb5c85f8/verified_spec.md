The function takes a sequence of integers and returns a pair. The first component is the sum of all elements, with the empty sequence summing to 0. The second component is the product of all elements, with the empty sequence product equal to 1.

Notes from formalizer:
- The Python request uses List[int] and Tuple[int, int]; the formal specification models the input as an integer sequence and the output as a pair of integers.
- The method is named sum_product to match the requested compiled Python entry point.
- Integer arithmetic is specified mathematically, without overflow behavior.
