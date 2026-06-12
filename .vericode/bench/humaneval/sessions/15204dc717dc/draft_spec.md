The function takes a nonempty sequence of real-valued polynomial coefficients in increasing degree order: the first coefficient is the constant term, the second is the coefficient of x, and so on. The input is restricted to have an even number of coefficients, a nonzero highest-degree coefficient, and at least one real root. The result is one real value at which the polynomial evaluates to zero. If the polynomial has multiple roots, any one such root may be returned.

Notes from formalizer:
- The original comment has a likely typo: it says xs[1] * x^2, but the implementation using enumerate means the term should be xs[2] * x^2. The specification follows the enumerate-based implementation.
- The guarantee that an even number of coefficients and a nonzero highest-degree coefficient implies a real root is assumed through an explicit root-existence precondition rather than proved from polynomial theory.
- No particular root-selection strategy is specified when multiple zeros exist; the specification permits any root.
- The numeric approximation behavior of the Python examples, such as rounding to two decimal places, is not part of the core specification.
