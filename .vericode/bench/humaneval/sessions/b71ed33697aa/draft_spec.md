For an input integer n between 1 and 1000 inclusive, return a pair of integers. The first component is the number of even-valued decimal palindromes k such that 1 <= k <= n. The second component is the number of odd-valued decimal palindromes k such that 1 <= k <= n. A number is considered a palindrome if its standard base-10 digit sequence reads the same forward and backward.

Notes from formalizer:
- The request says “range(1, n), inclusive,” which is ambiguous because Python range(1, n) normally excludes n. The examples include n, so this specification uses the inclusive interval 1 through n.
- The stated input constraint 1 <= n <= 10^3 is enforced as a precondition.
