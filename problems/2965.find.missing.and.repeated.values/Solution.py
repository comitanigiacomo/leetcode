from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        mappa = {}

        for row in grid:
            for num in row:
                if num in mappa:
                    mappa[num] += 1
                else:
                    mappa[num] = 1

        a, b = 0, 0
        for num in range(1, n * n + 1):
            if num not in mappa:
                b = num  
            elif mappa[num] == 2:
                a = num 

        return [a, b]
        
grid = [[1,3],[2,2]]
print(Solution().findMissingAndRepeatedValues(grid))
        