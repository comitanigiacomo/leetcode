from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            
            gold = grid[x][y]
            grid[x][y] = 0
            
            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))
            
            grid[x][y] = gold
            
            return gold + max_gold
        
        max_gold_collected = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold_collected = max(max_gold_collected, dfs(i, j))
        
        return max_gold_collected

grid = [[0,6,0],[5,8,7],[0,9,0]]
sol1 = Solution()
print(sol1.getMaximumGold(grid))
