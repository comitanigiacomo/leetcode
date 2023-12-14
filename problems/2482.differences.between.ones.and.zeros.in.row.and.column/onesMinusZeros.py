from typing import List
from collections import Counter

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



        
grid = [[0,1,1],[1,0,1],[0,0,1]]
sol1 = Solution()
result = sol1.onesMinusZeros(grid)
print(result)