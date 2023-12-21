from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max = 0
        for i in range(len(points)-1):
            if points[i+1][0]- points[i][0] > max :
                max = points[i+1][0]- points[i][0] 
        print(max)
        return max

points = [[8,7],[9,9],[7,4],[9,7]]
sol1 = Solution()
result = sol1.maxWidthOfVerticalArea(points)
print(result)



        
