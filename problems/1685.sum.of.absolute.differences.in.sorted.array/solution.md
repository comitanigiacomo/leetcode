# 1685.sum.of.absolute.differences.in.sorted.array

Here's the full description of the [problem](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/)

# Approach

The program initializes two variables, `left_sum` and `right_sum`, to keep track of the sums on the left and right sides of the current element. Then, for each element at index `i`, it calculates the absolute difference by considering the contribution from the left side and the right side. It updates the sums for the next iteration and stores the result in the output array `ans`. The final array `ans` contains the sum of absolute differences for each element in the input array nums.

# Complexity

- Time complexity:  O(n), where n is the length of the input array `nums`
- Space complexity: O(1)

# code

```python
from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        left_sum, right_sum = 0, sum(nums)

        for i in range(n):
            abs_diff = (i * nums[i] - left_sum) + (right_sum - (n - 1 - i + 1) * nums[i])
            ans.append(abs_diff)
            left_sum += nums[i]
            right_sum -= nums[i]

        return ans
```