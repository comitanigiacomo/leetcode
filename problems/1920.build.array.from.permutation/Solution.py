from typing import List 

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0, len(nums)):
            out.append(nums[nums[i]])
        return out

nums = [0,2,1,5,3,4]

sol1 = Solution()
print(sol1.buildArray(nums))
