# 2264.largest.3-same-digit.number.in.string

Here's the full description of the [problem](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/?envType=daily-question&envId=2023-11-19)


# Approach 

This code uses nested loops to consider all possible substrings of length 3 in the given string `num`. If a substring has three equal digits and is greater than the current maximum substring `max`, it updates the max substring. Finally, the function returns the largest substring found.
 
# Complexity 

- **Time complexity**: O(N^2), where `N` is the length of the input string `num`
- **Space complexity**: O(1)

## Code 

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max = ''
        for i in range(len(num)-2):
            
            for j in range(i+1, i+3):
                if num[i] != num[j]: break
                string = num[i: j+1]
                if len(string) == 3 and string > max: max = string
        return max
```
