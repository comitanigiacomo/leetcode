from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted = nums.sort()

        return (nums[len(nums)-1]*nums[len(nums)-2])-(nums[0]*nums[1])

nums = [5,6,2,7,4]
sol1 = Solution()
result = sol1.maxProductDifference(nums)
print(result)
