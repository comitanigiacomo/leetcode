# 1913.maximum.product.difference.between.two.pairs

Here's the full description of the [problem](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/?envType=daily-question&envId=2023-12-18)

# Approach

My idea consists of sorting the values in increasing order to instantly find the maximum and minimum product between two pairs, intending to return the maximum product difference.
# Complexity

- Time complexity: O(n log n) due to the sorting steps
- Space complexity: O(1)

# Code

```Python
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted = nums.sort()
        return (nums[len(nums)-1]*nums[len(nums)-2])-(nums[0]*nums[1])
```

