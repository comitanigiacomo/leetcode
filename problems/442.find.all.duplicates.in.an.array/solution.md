# 442.find.all.duplicates.in.an.array

Here's the full description of the [problem](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25)

# Approach

To solve the problem, I utilize the fact that integers in `nums` are within the range `[1, n]`. I iterate over `nums`, and at each step:

- I check if the element at position `abs(num)-1` (where `num` is the current element of the array) is negative.
- If it is negative, it means the element is a duplicate, so I add it to the `out` array.
- Otherwise, I negate it and continue iterating over the array.

# Complexity 

- Time complexity: O(n) where `n` is the length of the nums array

- Space complexiy: O(1)

# Code

```Python
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                out.append(abs(num))
            else:
                nums[index] = -nums[index]
        return out
```

