# 1630.arithmetic.subarrays

Here's the full description of the [problem](https://leetcode.com/problems/arithmetic-subarrays/description/?envType=daily-question&envId=2023-11-23)


# Approach

Given an array of integers `nums` and queries specified by ranges `[l[i], r[i]]`, the `checkArithmeticSubarrays` function iterates through each query, extracts the corresponding subarray, and checks if it can be rearranged to form an arithmetic sequence using the `is_arithmetic` function. The `is_arithmetic` function sorts the subarray and checks if the difference between consecutive elements is constant. The results are stored in the `out` list and returned.

# Complexity

- Time complexity: O(m * n * log(n)), where `m` is the number of queries, and `n` is the maximum length of a subarray
- Space complexity: O(n)

# code

```python
class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        out = []
        for idx, v in enumerate(l):
            arr = nums[v:r[idx] + 1]
            print(arr)
            out.append(self.is_arithmetic(arr))
        return out

    def is_arithmetic(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
```