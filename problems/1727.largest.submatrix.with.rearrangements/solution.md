# 1727.largest.submatrix.with.rearrangements

Here's the full description of the [problem](https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2023-11-26)


# Approach

The approach involves iterating through each row and updating the count of consecutive 1's in each column. 
For each row, sort the count array and calculate the maximum area considering the sorted count and the remaining width.
The overall maximum area is updated during the iterations.

# Complexity

- Time complexity: O(m * n * log(n)), where m is the number of rows and n is the number of columns.
- Space complexity: O(n)

# code

```python
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        count = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    count[j] = count[j] + 1 if i > 0 else 1
                else:
                    count[j] = 0

            sorted_count = sorted(count)
            for k in range(cols):
                max_area = max(max_area, sorted_count[k] * (cols - k))

        return max_area
```