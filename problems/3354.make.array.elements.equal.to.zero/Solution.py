from typing import List 
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        total_sum = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            left += nums[i]
            right = total_sum - left - nums[i]
            if nums[i] == 0:
                if left == right:
                    count += 2
                elif left == right - 1 or left == right + 1:
                    count += 1
        
        return count
        
nums = [1,0,2,0,3]
sol = Solution()
print(sol.countValidSelections(nums))
