# 2108.find.first.palindromic.string.in.the.array

Here's the full description of the [problem](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=daily-question&envId=2024-02-13)

# Approach

The program iterates through the given array of strings and checks each string if it is a palindrome using the isPalindrome function. The first palindrome found is returned. If no palindrome is found, an empty string is returned.

# Complexity

- Time complexity : O(n * m), where `n` is the number of words in the input list and `m` is the average length of the words.

- Space complexity :  O(1)

# Code

```Python
from ast import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for elem in words: 
            if self.isPalindrome(elem):
                return elem
        return ""


    def isPalindrome(self, s) -> bool:
        return s == s[::-1]   
```