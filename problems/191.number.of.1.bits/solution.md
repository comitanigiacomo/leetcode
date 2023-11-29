# 191.number.of.1.bits

Here's the full description of the [problem](https://leetcode.com/problems/number-of-1-bits/description/?envType=daily-question&envId=2023-11-29)

# Approach

The approach involves converting the integer `n` to its binary representation using the `bin()` function. Then, iterate through each bit of the binary string and count the number of '1' bits.

# Complexity

- Time complexity: O(n) where `n` is the length of the input
- Space complexity: O(1)

## Code

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:]  
        count = 0
        for bit in binary_str:
            if bit == '1':
                count += 1
        return count
```