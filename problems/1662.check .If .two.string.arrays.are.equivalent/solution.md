# 1662.check .If .two.string.arrays.are.equivalent

Here's the full description of the [problem](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/?envType=daily-question&envId=2023-12-01)

# Approach

To check if two string arrays are equivalent, I can concatenate the strings in both arrays and compare the resulting strings.

# Complexity

- Time complexity: O(N), where `N` is the total length of the concatenated strings.
- Space complexity: O(N)

# code

```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ''.join(word1)
        string2 = ''.join(word2)

        return string1 == string2      
```