The function takes an integer between 1 and 1000 inclusive and returns its lowercase Roman numeral representation. It uses the standard subtractive forms: iv for 4, ix for 9, xl for 40, xc for 90, cd for 400, and cm for 900. For example, 19 maps to xix, 152 maps to clii, and 426 maps to cdxxvi.

Notes from formalizer:
- Inputs outside the range 1 through 1000 are outside the specified contract and are not constrained.
- The specification assumes standard Roman numeral greedy decomposition with lowercase output.
- The main method is named int_to_mini_roman to match the requested compiled Python entry point.
