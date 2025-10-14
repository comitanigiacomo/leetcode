from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        if k == 1:
            return True
        
        count = 1
        tmp = []
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count +=1
            else:
                tmp.append(count + 1)
                count = 1
                
        tmp.append(count)   
                             
        for i in range(0, len(tmp)-1):
            if (tmp[i] >= k and tmp[i+1] >= k) or (tmp[i] >= 2*k):
                return True      

        return False

nums = [0,4,16,20,-6]
k = 2
sol = Solution()
print(sol.hasIncreasingSubarrays(nums, k))