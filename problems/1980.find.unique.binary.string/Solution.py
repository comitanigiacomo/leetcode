from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.result = None
        num_set = set(nums)
        self.backtrack("", num_set)
        
        return self.result

    def backtrack(self, current:str,nums: List[str]):
        if self.result is not None: return 

        if len(current) == len(nums):
            if current not in nums: 
                self.result = current
            return 
        
        for char in "01":
            self.backtrack(current + char, nums)
        
      
nums = ["01","10"]  
sol = Solution()
print(sol.findDifferentBinaryString(nums))