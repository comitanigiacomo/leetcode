# 141.linked.list.cycle

Here's the full description of the [problem](https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06)

# Approach


# Complexity

- Time complexity: 

- Space complexity: 

# Code 

```Python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        temp = self.head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
```