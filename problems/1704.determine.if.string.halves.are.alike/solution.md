# 1704.determine.if.string.halves.are.alike

Here's the full description of the [problem](https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12)

# Approach

The chosen approach involves splitting the string `s` into two halves and then counting the occurrences of vowels in each half. The function returns `True` if the counts are equal, indicating that the halves have the same number of vowels, and `False` otherwise.

# Complexity

- Time complexity: O(n), where `n` is the length of the input string
- Space complexity: O(1), as the size of the vowels list is constant.

# Code 

```Python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        str1 = s[:len(s)// 2]
        str2 = s [len(s)//2:]
        vowels1 = [str1.count(x) for x in "aeiouAEIOU"]
        vowels2 = [str2.count(x) for x in "aeiouAEIOU"]
    
        return sum(vowels1) == sum(vowels2)
```