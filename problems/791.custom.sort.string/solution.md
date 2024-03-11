# 791.custom.sort.string

Here's the full description of the [problem](https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11)

# Approach

The program sorts the characters of string `s` based on the specified order in string `order`. It accomplishes this by examining the characters in string `s` and placing them in the output string according to the order specified in `order`. Additionally, any remaining characters from `s` that are not present in `order` are appended to the result.

This approach efficiently sorts `s` in a custom manner based on the specified order.

# Complexity

- Time complexity: O(n + m), where `n` is the length of string order and `m` is the length of string `s`

- Space complexity: O(m), where `m` is the length of string `s`

# Code

```Python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        inOrder = ''
        out = ''
        chars = list(s)
        
        for elem in order: 
            for ch in s:
                if ch == elem: 
                    inOrder += elem
                    chars.remove(elem)
            
        return inOrder + out.join(chars)
```