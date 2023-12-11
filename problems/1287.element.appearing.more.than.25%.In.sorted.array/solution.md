# 1287.element.appearing.more.than.25%.In.sorted.array

Here's the full description of the [problem](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2023-12-11)

# Approach

Count the occurrences of each element in the array using `Counter`.
Then, iterate through the occurrences and return the element whose count exceeds one-fourth of the array's length

# Complexity

- Time complexity: O(N)
- Space complexity: O(N)

# Code

```Python 
from collections import Counter
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occurrences = Counter(arr)
        length = len(arr) // 4
        for elem, count in occurrences.items():
            if count > length:
                return elem
```