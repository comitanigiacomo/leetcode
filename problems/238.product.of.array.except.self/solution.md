# 238.product.of.array.except.self

Here's the ful description of the [problem](https://leetcode.com/problems/product-of-array-except-self/?envType=daily-question&envId=2024-03-15)

# Approach 

The approach used here is based on prefix and suffix products. We first calculate the prefix products of the input array, storing the product of all elements to the left of each element. Then, we calculate the suffix products of the input array, storing the product of all elements to the right of each element. Finally, we multiply the corresponding prefix and suffix products to get the final result.

# Complexity

- Time complexity: O(N), where `N` is the length of the input array

- Space complexity: O(1)

# Code

```Python 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0]*len(nums)
        product[0] = 1
        for i in range(1, len(nums)):
            product[i] = nums[i-1]*product[i-1]
        
        suffixProduct = 1
        
        for i in range(len(nums)-1, -1, -1):
            product[i] = product[i] * suffixProduct
            suffixProduct = suffixProduct * nums[i]
        return product
```