from typing import List

class Solution:
    def negative(self, nums):
        start, end = 0, len(nums)-1
        index = len(nums)

        while start <= end:
            mid = (start + end)// 2

            if nums[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid
                
        return index

    def positive(self, nums):
        start, end = 0, len(nums)-1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid -1
                index = mid
                
        return index

    def maximumCount(self, nums: List[int]) -> int:
        positive_count = len(nums) - self.positive(nums)
        negative_count = self.negative(nums)

        return max(positive_count, negative_count)
        
nums = [-2,-1,-1,1,2,3]
print(Solution().maximumCount(nums))   