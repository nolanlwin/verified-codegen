The function takes a rectangular grid of 0/1 values and a positive bucket capacity. For each row, it counts how many cells contain 1, treating that count as the amount of water in that well. It then computes how many bucket lowerings are needed for that row by rounding up water units divided by capacity. The final result is the sum of these per-row bucket counts.

Notes from formalizer:
- The computation is specified per row/well: bucket lowerings are summed after rounding up each row independently, rather than pooling water across all rows first.
- The constraint text `grid[:,1].length` is interpreted as the common row length/number of columns.
- The specification requires a nonempty rectangular grid with nonempty rows, binary cell values, and capacity in the stated range 1 through 10.
- Although the pure semantic definition is total for empty grids, the public method follows the stated input constraints and requires at least one row.
