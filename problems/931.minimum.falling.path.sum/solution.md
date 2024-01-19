# 931.minimum.falling.path.sum

Here's the full description of the [problem](https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19)

# Approach

The approach used here is dynamic programming. The idea is to iterate over the rows of the matrix and update each element by adding the minimum value among its adjacent elements in the previous row. This way, each element in the matrix will represent the minimum falling path sum ending at that position. Finally, the minimum value in the last row is the answer.

# Complexity

- Time complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix
- Space complexity: O(1)


# Code

```Python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += min(matrix[i-1][max(0, j-1):min(len(matrix[0]), j+2)])
        return min(matrix[-1])
```