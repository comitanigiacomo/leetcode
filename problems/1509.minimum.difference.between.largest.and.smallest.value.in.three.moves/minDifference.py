from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        sorted_nums = sorted(nums)
        
        min_diff = float('inf')
        for i in range(4):
            min_diff = min(min_diff, sorted_nums[-(4-i)] - sorted_nums[i])
        
        return int(min_diff)  
                
nums = [82,81,95,75,20]
sol = Solution()
print(sol.minDifference(nums))
