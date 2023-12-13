# 1582.special.positions.in.a.binary.matrix

Here's the full description of the [problem](https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2023-12-13)

# Approach

The approach involves iterating through each row in the matrix. For each row, it checks if the sum of elements in that row is equal to 1. If true, it finds the column index where the 1 is located and checks if the sum of elements in that column is also 1. If both conditions are satisfied, the position is considered special, and the count is incremented.

# Complexity

- Time complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix.
- Space complexity: O(1)

# Code

```Python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        special = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                special += get_column_sum(col_idx) == 1

        return special
```

