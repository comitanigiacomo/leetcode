# 2482.differences.between.ones.and.zeros.in.row.and.column

Here's the full description of the [problem](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/?envType=daily-question&envId=2023-12-14)

# Approach

The approach involves calculating the count of ones and zeros in each row and column and then computing the difference. The algorithm uses two separate lists for each row and column to store the count of ones and zeros. Finally, a new matrix is created to store the differences

# Complexity

- Time complexity: O(m * n) where `m` is the number of rows and `n` is the number of columns
- Space complexity: O (m * n)

# Code

```Python 
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        diff = [[0] * columns for _ in range(rows)]

        ones_row = [sum(row) for row in grid]
        zeros_row = [columns - ones for ones in ones_row]
        ones_col = [sum(row[j] for row in grid) for j in range(columns)]
        zeros_col = [rows - ones for ones in ones_col]

        for i in range(rows):
            for j in range(columns):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        return diff
```