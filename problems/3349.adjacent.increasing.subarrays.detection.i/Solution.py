from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        if k == 1:
            return True
        
        count = 0
        tmp = []
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count +=1
            else:
                tmp.append(count + 1)
                count = 0
                
        tmp.append(count + 1)   
                
        if len(tmp) == 1 and tmp[0] >= 2*k:
            return True
                             
        for i in range(1, len(tmp)):
            if (tmp[i] >= k and tmp[i-1] >= k) or (tmp[i] >= 2*k) or (tmp[i-1] >= 2*k):
                return True

        return False

nums = [0,4,16,20,-6]
k = 2
sol = Solution()
print(sol.hasIncreasingSubarrays(nums, k))