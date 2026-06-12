The function accepts a sequence of non-negative integers and returns a new sequence sorted in ascending order by the number of 1 bits in each integer’s standard binary representation. If two integers have the same number of 1 bits, they are ordered by their numeric value in ascending order.

Notes from formalizer:
- The written requirement says the input consists of non-negative integers, so the specification requires every element to be non-negative.
- The provided negative-number example conflicts with the non-negative input requirement and is outside this specification’s precondition.
- The provided positive examples appear to show ordinary numeric sorting, not sorting by number of binary 1 bits. Under the stated bit-count rule, [1, 5, 2, 3, 4] would sort to [1, 2, 4, 3, 5], and [1, 0, 2, 3, 4] would sort to [0, 1, 2, 4, 3].
- The specification follows the textual bit-count sorting rule rather than the inconsistent example outputs.
