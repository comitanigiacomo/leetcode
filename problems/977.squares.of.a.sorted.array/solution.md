# 977.squares.of.a.sorted.array

Here's the full description of the [problem](https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-03-02)

# Approach

The programs simply iterates over `nums` and replaces each numbers with its square. Lastly it uses the `sort` method to return the obtained array in non-decreasing order

# Complexity

- Time complexity: O(nlog(n)), where `n` is the lenght of `nums`

- Space complexity: O(n)

# Code

```Python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = [elem*elem for elem in nums]
        out.sort()
        return out
```