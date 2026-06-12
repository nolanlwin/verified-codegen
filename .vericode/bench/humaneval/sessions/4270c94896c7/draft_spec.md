The function accepts a nonnegative integer n and returns the n-th Fibonacci number, using the standard definition: fib(0) = 0, fib(1) = 1, and fib(n) = fib(n - 1) + fib(n - 2) for n >= 2. For example, fib(10) returns 55, fib(1) returns 1, and fib(8) returns 21.

Notes from formalizer:
- The behavior for negative inputs is not specified by the request, so the specification restricts inputs to n >= 0.
- The examples imply the standard zero-based Fibonacci sequence, so fib(0) is specified as 0.
