from pyparsing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
        
        
        
            