from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
      
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        
       
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        score = 0
        for i in range(m):
            for j in range(n):
                score += grid[i][j] * (1 << (n - 1 - j))
        
        return score

grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
sol = Solution()
print(sol.matrixScore(grid))
