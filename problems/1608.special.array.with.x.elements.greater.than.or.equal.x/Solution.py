from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        for i in range (1, len(nums)+1):
            count = 0
            for elems in nums: 
                if elems >= i : 
                    count += 1
            if count == i : return i

        return -1
   
nums = [3,5]
sol1 = Solution()
print(sol1.specialArray(nums))