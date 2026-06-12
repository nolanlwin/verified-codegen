The function accepts a non-negative integer n and returns the sequence of all prime integers strictly less than n, in increasing order. Values 0 and 1 are not prime, so inputs 0, 1, and 2 return an empty sequence. For example, input 20 returns [2, 3, 5, 7, 11, 13, 17, 19].

Notes from formalizer:
- The docstring says "first n integers that are prime numbers and less than n," but the examples indicate the intended behavior is to return all prime numbers strictly less than n, not the first n primes.
- The specification uses an integer sequence as the result model rather than a mutable array.
- The method is named count_up_to to match the requested Python-facing name.
