# 876.middle.of.the.linked.list

Here's the full description of the [problem](https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=daily-question&envId=2024-03-07)

# Approach

The problem can be efficiently solved using the two-pointer technique: one `slow` pointer and one `fast` pointer. `slow` moves one step at a time while `fast` moves two steps at a time. By the time `fast` reaches the end of the list, `slow` will be at the middle of the list.

# Complexity

- Time complexity: O(n) where `n` is the number of nodes in the linked list

- Space complexity: O(1)

# Code 

```Python

#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```