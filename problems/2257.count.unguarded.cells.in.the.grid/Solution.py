from typing import List
from collections import defaultdict

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for r,c in walls:
            grid[r][c] = 1

        for r,c in guards:
            grid[r][c] = 2

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc

                while 0 <= r < m  and 0 <= c < n:
                    if grid[r][c] == 1 or grid[r][c] == 2:
                        break

                    if grid[r][c] == 0:
                        grid[r][c] = 3

                    r += dr
                    c += dc

        unguarded = sum(cell == 0 for row in grid for cell in row)
        return unguarded 

m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
sol = Solution()
print(sol.countUnguarded(m, n, guards, walls))
