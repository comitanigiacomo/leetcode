from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        out = 0
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        remainder_count = [0] * k
        for i in range(n + 1):
            remainder = prefix_sum[i] % k
            out += remainder_count[remainder]
            remainder_count[remainder] += 1
        return out
                
        
        
nums = [4,5,0,-2,-3,1]
k = 5
sol = Solution()
print(sol.subarraysDivByK(nums,k))