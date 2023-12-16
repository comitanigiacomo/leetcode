# 242.valid.anagram

Here's the full description of the [problem](https://leetcode.com/problems/valid-anagram/description/?envType=daily-question&envId=2023-12-16)

# Approach

The program sorts the strings `t` and `s`, and returns `True` if the resulting sorted strings are equal, `False` otherwise

# Complexity

- Time complexity: O(n log n) due to the sorting steps
- Space complexity: O(n) due to the space required for the sorted strings

# Code

```Python 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
