# Sicuramente devo sfruttare il fatto che è binario

# Devo trovare un modo per iterare sull'array il meno possibile. 

# Uso due puntatori che si muovono all'interno dell'array 



from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        out = 0
        curr = 0 
        for i in range(0, len(nums)-1):
            if nums[i] == goal:
                out += 1
            curr += nums[i]
            if i > 0 : 
                for j in range(0,i):
                    if curr - nums[i-1] == goal: out += 1
        return out 
                
                
                
nums = [0,0,0,0,0]
goal = 0
sol1 = Solution()
print(sol1.numSubarraysWithSum(nums, goal))