The function takes a nonempty string representing a valid decimal number and returns the nearest integer. A valid input may have an optional leading minus sign, must contain digits before any decimal point, and if a decimal point is present it must be followed by at least one digit. The returned integer is computed by rounding to the nearest integer, with exact half cases rounded away from zero: for example, "14.5" maps to 15 and "-14.5" maps to -15.

Notes from formalizer:
- The previous type error was caused by comparing a character to the string literal "9"; this skeleton consistently uses character literals such as '9'.
- The specification conservatively excludes leading plus signs, whitespace, exponent notation, missing integer parts such as ".5", and trailing decimal points such as "1.".
- The method body is intentionally left unimplemented with an assumption placeholder; all observable behavior is specified by the postcondition linking the result to ClosestIntegerSpec.
