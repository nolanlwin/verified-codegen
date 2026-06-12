The function takes three numeric inputs and returns true exactly when all three inputs are integer-valued and one of them is equal to the sum of the other two. It returns false otherwise.

Notes from formalizer:
- The specification models inputs as exact mathematical numeric values and treats a value as an integer if it is equal to some integer. Under this interpretation, a value like 3.0 is considered integer-valued.
- If the intended Python behavior is to reject all float-typed values even when they represent whole numbers, a richer input model distinguishing runtime numeric types would be needed.
- The specification uses exact arithmetic, so it does not model floating-point rounding behavior.
