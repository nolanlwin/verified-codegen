The function returns true exactly when the input array can be made non-decreasing by applying zero or more right rotations. The empty array returns true. The specification characterizes this by counting circular descents: positions where an element is greater than the next element, treating the last element as followed by the first. A sequence is accepted when this circular descent count is at most one.

Notes from formalizer:
- The prompt states that input elements are unique, but the specification does not require or enforce uniqueness; the same circular-descent characterization also works for arrays with duplicate values under non-decreasing order.
- Right shifts by any number of positions are treated as arbitrary rotations of the array, including zero shifts.
