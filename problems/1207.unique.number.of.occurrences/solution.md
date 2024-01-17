# 1207.unique.number.of.occurrences

Here's the full description of the [problem](https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17)

# Approach

The approach taken here is to use a dictionary to count the frequency of each number in the array. After that, a set is used to store the unique frequencies. If the length of the set of frequencies is equal to the length of the frequency dictionary, it means that the number of occurrences of each value is unique.

# Complexity

- Time complexity : O(N), where `N` is the length of the input array `arr`
- Space complexity : O(N)

# Code

```Python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        frequency = {}
        freqOfSet = set()
    
        for i in arr:
            frequency[i] = frequency.get(i, 0) + 1
    
        for f in frequency.values():
            freqOfSet.add(f)
    
        return len(freqOfSet) == len(frequency)     
```
