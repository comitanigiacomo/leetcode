# 1171.remove.zero.sum.consecutive.nodes.from.linked.list

Here's the full description of the [problem](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-03-12)

# Approach

The problem requires removing consecutive nodes from a linked list that sum up to zero. The program traverses the linked list while maintaining the running prefix sum. If it encounters a prefix sum that it has seen before, it means that the nodes in between contribute zero to the sum, so it can remove those nodes.

After processing the entire linked list, it iterates through it again, adjusting the next pointers of the nodes to remove the consecutive nodes that sum up to zero.

# Complexity

- Time complexity: O(n), where `n` is the number of nodes in the linked list.

- Space complexity: O(n).

# Code

```Python
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        
        current = dummy
        
        while current:
            prefix_sum += current.val
            prefix_sums[prefix_sum] = current
            current = current.next
        
        prefix_sum = 0
        current = dummy
        
        while current:
            prefix_sum += current.val
            current.next = prefix_sums[prefix_sum].next
            current = current.next
        
        return dummy.next
```