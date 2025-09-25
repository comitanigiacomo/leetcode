from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 1):
            level = triangle[i+1]
            
            for j in range(1, len(level) - 1):
                level[j] = min(level[j] + triangle[i][j],
                               level[j] + triangle[i][j-1])
            
            level[0] += triangle[i][0]
            level[-1] += triangle[i][-1]
        
        return min(triangle[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
sol = Solution()
print(sol.minimumTotal(triangle))
        