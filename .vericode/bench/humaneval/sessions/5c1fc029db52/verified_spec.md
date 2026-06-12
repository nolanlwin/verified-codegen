For a nonnegative number n, there are n cars traveling left-to-right and n cars traveling right-to-left. Since every car from one group eventually meets every car from the other group exactly once, and collisions do not alter trajectories, the required result is the total number of cross-direction pairs, which is n squared.

Notes from formalizer:
- The input is specified as requiring n >= 0, since a negative number of cars is not meaningful.
- The recursive specification computes n^2 via the recurrence f(0) = 0 and f(n) = f(n - 1) + 2n - 1 for n > 0.
