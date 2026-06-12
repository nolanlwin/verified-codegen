The function returns a transformed copy of the input string. Every maximal consecutive run of spaces is replaced as follows: a run of one space becomes one underscore, a run of two spaces becomes two underscores, and a run of three or more spaces becomes a single hyphen. All non-space characters are preserved in their original order.

Notes from formalizer:
- The phrase “replace all consecutive spaces with -” is interpreted as replacing each run of more than two consecutive spaces with one single hyphen, matching the provided example `" Example   3" -> "_Example-3"`.
- Runs of exactly two spaces are specified as two underscores, by extending the rule that spaces are replaced with underscores unless the run length is greater than two.
- The semantic function carries an extra `pendingSpaces` parameter; the public method uses it with initial value 0.
