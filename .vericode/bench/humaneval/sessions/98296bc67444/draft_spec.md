The function takes an integer and returns true exactly when the integer is the cube of some integer. Negative inputs are handled by checking the cube property of their absolute value, since a negative number is a cube exactly when its absolute value is a cube. Zero is considered a cube.

Notes from formalizer:
- The request says the input is always valid; since the input type is an integer, no additional input preconditions are needed.
- The specification treats negative cubes symmetrically via absolute value, so -1, -8, -27, etc. are accepted.
- The method is named `iscube` to match the requested compiled Python entry point.
