from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = len(nums)

        for i in range(len(nums)):
            elem = nums[i]
            if elem < 0: neg += 1
            if elem > 0: 
                pos = i
                break
        return max(neg, len(nums)-pos)
        
nums = [-2,-1,-1,1,2,3]
print(Solution().maximumCount(nums))   