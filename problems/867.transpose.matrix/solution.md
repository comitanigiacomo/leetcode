# 867.transpose.matrix

Here's the full description of the [problem](https://leetcode.com/problems/transpose-matrix/description/?envType=daily-question&envId=2023-12-10)

# Approach

The approach is to create a new matrix (`transposed`) where the number of rows is equal to the number of columns of the original matrix, and the number of columns is equal to the number of rows of the original matrix. Then, iterate through each element of the original matrix and assign it to the corresponding position in the `transposed` matrix.

# Complexity

- Time complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns in the original matrix.
- Space complexity: O(m * n)

# Code

```Python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]
        
        return transposed
```