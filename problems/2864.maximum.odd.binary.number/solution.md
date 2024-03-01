# 2864.maximum.odd.binary.number

Here's the full description of the [problem](https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01)

# Approach

My idea is to sorts the string in descending order so that all the '1's are positioned on the leftmost side. Then, the program checks if the last character is '1', and if not, it iterates over the string from right to left to find the first occurrence of '1'. Once found, it swaps the last character with the first '1' encountered, thus ensuring the maximum odd binary number is obtained.

# Complexity

- Time complexity: O(nlogn) time, where `n` is the length of the string

- Space complexity: O(n)

# Code 

```Python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = list(s)
        l.sort(reverse=True)
        str_sorted = ''.join(l)
        if str_sorted[-1] != '1':
            for i in range(len(str_sorted) - 1, -1, -1):
                if str_sorted[i] == '1':
                    str_sorted = str_sorted[:i] + str_sorted[-1] + str_sorted[i+1:-1] + str_sorted[i] 
                    break
        return str_sorted
```