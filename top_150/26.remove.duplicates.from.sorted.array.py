from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = len(nums)-1
        k = 2
        for i in range(1,len(nums)): 
            if nums[i] == nums[i-1] :
                nums[j],nums[i] = nums[i], nums[j]
                j-= 1
            if nums[i] > nums[k] :
                nums[k],nums[i] = nums[i], nums[k]
                k+= 1
            
            
        return j
nums =[0,0,1,1,1,2,2,3,3,4]
sol1 = Solution() 

result = sol1.removeDuplicates(nums)
print(result)
print(nums[:result])


