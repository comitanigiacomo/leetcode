# 1903.largest.odd.number.in.string

Here's the full description of the [problem](https://leetcode.com/problems/largest-odd-number-in-string/description/)

# Approach

The approach of the solution involves iterating through the characters of the input string in `reverse order`. For each character, it checks if it is an odd digit. If an odd digit is found, it returns the substring of the original string from the beginning up to that character. If no odd digit is found, an empty string is returned.

# Complexity

- Time complexity: O(N), where `N` is the length of the input string `num`
- Space complexity: O(1)

# Code 

```Python
class Solution:
    def largestOddNumber(self, num: str) -> str:
      count = len(num)-1
      for char in reversed(num):
        if int(char) % 2 != 0:  
          return num[:count+1]
        count -= 1
      return ''               
```