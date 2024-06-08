from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1} 
        total_sum = 0

        for i, num in enumerate(nums):
            total_sum += num
            
            if k != 0:
                remainder = total_sum % k
            else:
                remainder = total_sum

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:  
                    return True
            else:
                remainder_map[remainder] = i

        return False
        
nums = [23, 2, 6, 4, 7]
k = 13
sol1 = Solution()
print(sol1.checkSubarraySum(nums, k)) 
