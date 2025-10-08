import heapq
from typing import List
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        out = [1] * len(rains)
        full = set()
        future = defaultdict(list)
        
        for i, r in enumerate(rains):
            if r > 0:
                future[r].append(i)
        
        pq = []
        
        for i, r in enumerate(rains):
            if r > 0:
                if r in full:
                    return []
                full.add(r)
                future[r].pop(0)
                if future[r]:
                    heapq.heappush(pq, (future[r], r))
                else:
                    _, lake = heapq.heappop(pq)
                    out[i] = lake
                    full.remove(lake)
                    
        return out
                
rains = [1,2,0,0,2,1]
sol = Solution()
print(sol.avoidFlood(rains))