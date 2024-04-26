from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        dp = grid[0][:]
        
        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                min_val = float('inf')
                for k in range(n):
                    if k != j:
                        min_val = min(min_val, dp[k])
                new_dp[j] = grid[i][j] + min_val
            dp = new_dp  
        
        return min(dp)

grid = [[1,2,3],[4,5,6],[7,8,9]]
sol1 = Solution()
print(sol1.minFallingPathSum(grid))
