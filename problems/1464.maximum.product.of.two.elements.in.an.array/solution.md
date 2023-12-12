# 1464.maximum.product.of.two.elements.in.an.array

Here's the full description of the [problem](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2023-12-12)

# Approach

The approach used in this solution is to sort the given array in ascending order. After sorting, the two largest elements will be at the end of the array. The maximum product of two elements can then be obtained by subtracting 1 from each of these largest elements and multiplying them.

# Complexity

- Time complexity: O(n log n) 
- Space complexity: O(1)

# Code

```Python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
```