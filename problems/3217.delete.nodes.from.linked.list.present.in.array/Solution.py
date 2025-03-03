from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a set from nums for O(1) lookups
        nums_set = set(nums)
        
        # Create a dummy node to simplify edge cases where head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        # Traverse the linked list
        while curr:
            if curr.val in nums_set:
                # Remove current node
                prev.next = curr.next
            else:
                # Move prev pointer to current
                prev = curr
            # Move to the next node
            curr = curr.next
        
        # Return the updated list, starting at dummy.next
        return dummy.next
        
