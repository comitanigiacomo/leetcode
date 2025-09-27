from itertools import combinations
from typing import List

class Solution:
        
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        max_area = 0.0
        
        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            
            area = 0.5 * abs(
                x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
            )
        
            max_area = max(max_area, area)
            
        return max_area
        
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
sol = Solution()
print(sol.largestTriangleArea(points))
