




from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0]*len(nums)
        product[0] = 1
        for i in range(1, len(nums)):
            product[i] = nums[i-1]*product[i-1]
        
        suffixProduct = 1
        
        for i in range(n-1, -1, -1):
            product[i] = product[i] * suffixProduct
            suffixProduct = suffixProduct * nums[i]
        return product
        