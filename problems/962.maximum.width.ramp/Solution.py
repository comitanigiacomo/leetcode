from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_ramp = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_ramp = max(max_ramp, j - stack.pop())
        
        return max_ramp
    
nums = [6,0,8,2,1,5]
sol = Solution()
print(sol.maxWidthRamp(nums))