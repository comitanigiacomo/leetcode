# 19.remove.nth.node.from.end.of.list

Here's the full description of the [problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03)

# Approach

To remove a node in a linked list, it is possible to consider the node preceding the one to be removed and ensure that it points to the node succeeding the one to be removed. It is important to note that it is useful to handle the case where the node to be removed is the head of the linked list: in that case, simply setting the next node as the head of the list is sufficient.

# Complexity

- Time complexity: O(n), where `n` is the number of nodes in the linked list

- Space complexity: O(1)

# Code 

```Python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Calulate the lenght of the linked list
        curr1 = head
        lenght = 1
        while curr1.next is not None:
            curr1 = curr1.next 
            lenght += 1
        
        count = 0
        curr = head 

        # If i have to delete the first node of the list, i can move forward the head of the list
        if n == lenght:
            head = head.next
            return head 
        
        while curr.next is not None: 
            if count == lenght-n-1:
                curr.next = curr.next.next
                return head
            count += 1
            curr = curr.next
```