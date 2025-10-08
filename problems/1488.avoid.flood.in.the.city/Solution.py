import heapq
from typing import List
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        out = [1] * n
        full = set()
        future = defaultdict(list)
        
        for i, r in enumerate(rains):
            if r > 0:
                future[r].append(i)
                
        pq = []

        for i, r in enumerate(rains):
            if r > 0:
                out[i] = -1
                if r in full:
                    return []
                full.add(r)
                future[r].pop(0)
                if future[r]:
                    heapq.heappush(pq, (future[r][0], r))
            else:
                if pq:
                    next_day, lake = heapq.heappop(pq)
                    out[i] = lake
                    full.remove(lake)
                else:
                    out[i] = 1
        return out
                
rains = [1,2,0,0,2,1]
sol = Solution()
print(sol.avoidFlood(rains))