from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        x = len(nums)
        for i in range(1 << x):
            out.append([nums[j] for j in range(x) if (i & (1 << j))])
        return out
    
nums = [1,2,3]
sol1 = Solution()
print(sol1.subsets(nums))