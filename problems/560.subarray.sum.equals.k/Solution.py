from collections import defaultdict
from typing import DefaultDict, List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1

        for num in nums:
            prefix += num
            count += prefix_freq[prefix - k]
            prefix_freq[prefix] += 1

        return count


nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))
