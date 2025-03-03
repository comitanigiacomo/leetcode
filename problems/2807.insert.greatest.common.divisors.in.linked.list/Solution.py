import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next

        while curr :
            tmp = math.gcd(prev.val, curr.val)
            dummy = ListNode(tmp)
            
            prev.next = dummy
            dummy.next = curr

            prev = curr
            curr = curr.next

        return head
        