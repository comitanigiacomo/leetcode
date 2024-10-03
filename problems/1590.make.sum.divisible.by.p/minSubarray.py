from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
                
        if remainder == 0: return 0
        
        prefix_map = {0:-1}
        prefix_sum = 0
        min_length = len(nums)
        
        for i,num in enumerate(nums):
            prefix_sum += num
            current_remainder = prefix_sum % p
            
            target_remainder = (current_remainder - remainder) % p
                        
            if target_remainder in prefix_map: 
                min_length = min(min_length, i - prefix_map[target_remainder])
                
            prefix_map[current_remainder] = i
            
        return min_length if min_length < len(nums) else -1

nums = [3,1,4,2]
p = 6
sol = Solution()
print(sol.minSubarray(nums, p))