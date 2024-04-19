# Idea: effettuando una BFS, controllo per ogni 1 se questo è circondato da acqua nelle 4 direzioni.
# Dove non lo è, sposto la bfs su quella direzione e itero il procedimento, fino  a quando non ho visitato tutti gli 1 adiacenti
# La BFS si ferma quando ha visitato tutti gli uni, e , nel caso in cui 

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, row, col):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            queue = [(row, col)]
            while queue:
                r, c = queue.pop(0)
                grid[r][c] = "0"  
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"  

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    bfs(grid, i, j)
                    num_islands += 1

        return num_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

sol1 = Solution()
print(sol1.numIslands(grid))