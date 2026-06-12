The function takes a sequence of numeric GPAs and returns a sequence of letter grades of the same length and in the same order. Each GPA is classified by the first matching rule: exactly 4.0 maps to A+; greater than 3.7 to A; greater than 3.3 to A-; greater than 3.0 to B+; greater than 2.7 to B; greater than 2.3 to B-; greater than 2.0 to C+; greater than 1.7 to C; greater than 1.3 to C-; greater than 1.0 to D+; greater than 0.7 to D; greater than 0.0 to D-; and all remaining values to E.

Notes from formalizer:
- The GPA values are modeled as real numbers because the input uses decimal GPAs.
- The grading table is interpreted as an ordered threshold chain. In particular, only exactly 4.0 maps to A+; values greater than 4.0 would match the next rule and map to A.
- No validity precondition is imposed on GPA range; nonpositive values map to E.
