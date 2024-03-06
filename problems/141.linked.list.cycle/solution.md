# 141.linked.list.cycle

Here's the full description of the [problem](https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06)

# Approach

The program uses two pointers to check if there is a cycle in the linked list

# Complexity

- Time complexity: O(n) where `n` is the number of nodes in the linked list

- Space complexity: O(1)

# Code 

```Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head: return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if fast == slow: return True
            slow = slow.next 
            fast = fast.next.next 
        return False
```