from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                out.append(abs(num))
            else:
                nums[index] = -nums[index]
        return out
              
nums = [4,3,2,7,8,2,3,1]
sol1 = Solution()
print(sol1.findDuplicates(nums))