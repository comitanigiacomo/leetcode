from typing import List 
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted((w / q, q) for w, q in zip(wage, quality)) 
        
        heap = []  
        total_quality = 0
        min_cost = float('inf')
        
        for ratio, q in workers:
            total_quality += q
            heapq.heappush(heap, -q) 
            
            if len(heap) > k:
                total_quality += heapq.heappop(heap) 
            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        
        return min_cost

        
quality = [10,20,5]
wage = [70,50,30]
k = 2
sol1 = Solution()
print(sol1.mincostToHireWorkers(quality,wage,k))