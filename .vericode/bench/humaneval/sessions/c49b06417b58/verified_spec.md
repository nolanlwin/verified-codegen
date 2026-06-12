The function takes a triangle side length and its corresponding height and returns the triangle's area, computed as one half of side times height. For example, inputs 5 and 3 produce 7.5.

Notes from formalizer:
- The specification uses real-valued inputs and output to support fractional areas such as 7.5.
- No precondition is imposed requiring nonnegative side length or height, because the original Python request does not state how negative inputs should be handled.
- The main method is named `triangle_area` to match the expected compiled Python entry point.
