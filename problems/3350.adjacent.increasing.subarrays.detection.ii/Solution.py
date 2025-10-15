from typing import List
from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0

        subarray_lengths = []
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_length += 1
            else:
                subarray_lengths.append(current_length)
                current_length = 1
        
        subarray_lengths.append(current_length)

        if len(subarray_lengths) == 1:
            return subarray_lengths[0] // 2

        max_result = subarray_lengths[0] // 2
        
        for i in range(1, len(subarray_lengths)):
           
            split_candidate = subarray_lengths[i] // 2
            
            merge_candidate = min(subarray_lengths[i], subarray_lengths[i-1])
            
            max_result = max(max_result, split_candidate, merge_candidate)
            
        return max_result
    
nums = [2,5,7,8,9,2,3,4,3,1]
sol = Solution()
print(sol.maxIncreasingSubarrays(nums))
        