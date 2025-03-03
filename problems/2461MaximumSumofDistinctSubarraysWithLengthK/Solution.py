from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        current_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            current_sum += nums[i]

            if i >= k:
                oldest = nums[i-k]
                freq[oldest] -= 1
                if freq[oldest] == 0:
                    del freq[oldest]
                    current_sum -= oldest

            if len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum





