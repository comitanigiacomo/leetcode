# 1611.minimum.one.bit.operations.to.make.integers.zero

Here's the full description of the [problem](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2023-11-30)


# Approach

The approach here is to use bitwise operations to manipulate the bits of the given integer. The key idea is to iteratively perform operations until the number becomes zero. The bitwise XOR and AND operations are used to manipulate the bits.

# Complexity

- Time complexity: O(logN)
- Space complexity: O(1)

# code

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)
```