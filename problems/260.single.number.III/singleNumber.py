from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            if nums[i]  in out :
                out.remove(nums[i])
            else:
                out.append(nums[i])
        return out
        
nums = [-1, 0]
sol1 = Solution()
print(sol1.singleNumber(nums))
