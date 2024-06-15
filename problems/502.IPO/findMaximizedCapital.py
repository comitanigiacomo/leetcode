import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        max_heap = []
        j = 0

        for _ in range(k):
            while j < len(projects) and projects[j][1] <= w:
                heapq.heappush(max_heap, -projects[j][0])
                j += 1
            
            if not max_heap:
                break
            
            w += -heapq.heappop(max_heap)
        
        return w
 
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
sol1 = Solution()
print(sol1.findMaximizedCapital(k,w,profits,capital))