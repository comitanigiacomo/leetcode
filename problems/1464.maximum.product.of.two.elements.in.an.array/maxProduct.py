from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
    
nums = [3,4,5,2]
sol1 = Solution()
result = sol1.maxProduct(nums)
print(result)