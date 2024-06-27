from typing import List
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]

edges = [[1,2],[2,3],[4,2]]   
sol1 = Solution()
print(sol1.findCenter(edges))
        