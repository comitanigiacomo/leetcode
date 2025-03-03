from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        left_sum, right_sum = 0, sum(nums)

        for i in range(n):
            abs_diff = (i * nums[i] - left_sum) + (right_sum - (n - 1 - i + 1) * nums[i])
            ans.append(abs_diff)
            left_sum += nums[i]
            right_sum -= nums[i]

        return ans