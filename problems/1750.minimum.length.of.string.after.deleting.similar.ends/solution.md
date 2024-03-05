# 1750.minimum.length.of.string.after.deleting.similar.ends

Here's the full description of the [problem](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05)

# Approach

The approach to solve this problem involves using two pointers, one starting from the beginning of the string (`left`) and the other starting from the end of the string (`right`). The program moves these pointers towards each other, checking if the characters at the current positions are the same. If they are, continues moving the pointers towards the center until it find two different characters or until the pointers meet.

At each step, updates the pointers to skip over consecutive characters that are the same from both ends. Finally, returns the length of the remaining substring between the pointers.

# Complexity

- Time complexity: O(n), where `n` is the length of the input string

- Space complexity: O(1)

# Code

```Python
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char: 
                right -= 1
        
        return right -left +1
```