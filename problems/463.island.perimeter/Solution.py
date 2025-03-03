from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                #Per ogni pezzo di terra guardo se confina in tutte e quattro le direzioni.
                #Per ogni confine, tolgo un perimetro
                sum = 4
                if grid[i][j] == 1 : 
                    if i != 0 and grid[i-1][j] == 1: 
                        sum -= 1
                    if i != len(grid)-1 and grid[i+1][j] == 1: 
                        sum -= 1
                    if j != 0 and grid[i][j-1] == 1: 
                        sum -= 1
                    if j != len(grid[i]) - 1 and grid[i][j+1] == 1: 
                        sum -= 1
                    perimeter += sum
        return perimeter
                
                
         
         
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sol1 = Solution()
print(sol1.islandPerimeter(grid))