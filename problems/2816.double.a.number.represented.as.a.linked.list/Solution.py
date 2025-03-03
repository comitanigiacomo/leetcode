from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        if head.val >= 5 :
            head = ListNode(1, head)    
        while current :
            current.val = (current.val * 2) % 10
            if current.next:
                successivo = current.next 
                if (successivo.val * 2 ) >= 10: current.val = current.val + 1 
            current = current.next 
        return head
        
            
        
