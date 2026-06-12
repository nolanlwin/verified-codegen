The function accepts an integer n greater than 1 that is assumed not to be prime. It returns the largest positive divisor of n that is prime. The intended behavior matches examples such as returning 29 for 13195 and 2 for 2048.

Notes from formalizer:
- The precondition excludes prime inputs and values less than or equal to 1, matching the request’s assumption.
- For composite inputs, the specification defines the result by searching downward from n - 1 for the first divisor that is prime.
- The method name is kept as largest_prime_factor to match the requested Python-facing name.
