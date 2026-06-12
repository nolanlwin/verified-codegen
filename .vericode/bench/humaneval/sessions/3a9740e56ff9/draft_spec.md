The function takes a non-negative integer n and returns the n-th value of the FibFib sequence. The sequence is defined by base cases fibfib(0) = 0, fibfib(1) = 0, and fibfib(2) = 1. For every n greater than or equal to 3, the result is the sum of the previous three sequence values: fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

Notes from formalizer:
- The specification restricts inputs to non-negative integers; behavior for negative inputs is intentionally unspecified.
- The request asks for efficient computation, but this skeleton specifies only the required mathematical behavior and leaves implementation absent via the empty assumed body.
- The method is named `fibfib` to match the expected compiled Python entry point.
