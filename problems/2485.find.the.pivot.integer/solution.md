# 2485.find.the.pivot.integer

Here's the full description of the [problem](https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13)

# Approach

To find the pivot integer, the program leverages the fact that the sum of the first x positive integers can be calculated using the formula 
$$
\frac{x \cdot (x + 1)}{2}
$$

The program calculates the expected sum of elements from 1 to `x` using this formula and compares it with the sum of elements from `x` to `n`. If they are equal, the program returns `x` as the pivot integer.

Otherwise, if the sums are not equal, it returns -1.

# Complexity

- Time complexity: O(sqrt(n)). 

- Space complexity: O(1)

# Code

```Python
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)    
```