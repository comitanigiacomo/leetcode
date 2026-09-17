from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                operations += 1
            res += operations
        return res
    
sol = Solution()
nums = [5, 3, 2]
print(sol(nums))