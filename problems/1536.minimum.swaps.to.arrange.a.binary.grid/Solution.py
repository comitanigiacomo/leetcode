from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # first i wanna find the right one's
        
        n = len(grid)
        pos = []
        
        for row in grid:
            last_one = -1
            
            for i in range(n-1, -1, -1):
                if row[i] == 1:
                    last_one = i
                    break
            pos.append(last_one)
            
        # now i can simulate the swaps and find if there is a solution
        # since i only wanna see if the grod is ok, i dnt have to do a full bubble sort
        # I can accept a greedy solution
        
        swaps = 0
        
        for i in range(n):
            target = i
            found = False
            
            for j in range(i, n):
                if pos[j] <= target:
                    found = True
                    
                    for k in range(j, i, -1):
                        pos[k], pos[k-1] = pos[k-1], pos[k]
                        swaps += 1
                    break
        
        if not found:
            return -1
        
        return swaps
    
grid = [[0,0,1],[1,1,0],[1,0,0]]
sol = Solution()

print(sol.minSwaps(grid))