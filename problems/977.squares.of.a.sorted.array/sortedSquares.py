from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = [elem*elem for elem in nums]
        out.sort()
        return out

nums = [-4,-1,0,3,10]      
sol1 = Solution()
print(sol1.sortedSquares)