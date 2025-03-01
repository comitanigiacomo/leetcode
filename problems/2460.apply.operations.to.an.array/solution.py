from typing import List 

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0

        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums 
        
        
nums = [1,2,2,1,1,0]
sol = Solution()
print(sol.applyOperations(nums))     


# You can check my solution's explanation by clicking [here](https://leetcode.com/problems/apply-operations-to-an-array/solutions/6483184/easy-solution-by-giacomoleetcode-w8cs/)  