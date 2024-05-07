class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        string_num = ''
        current = head
        while current: 
            string_num = string_num + str(current.val)
            current = current.next
        
        num = int(string_num) * 2
        lst = [int(i) for i in str(num)]

        current = head 
        i = 0
        while i < len(lst):
            current.val = lst[i]
            if current.next is None:
                if i < len(lst) - 1:
                    current.next = ListNode(0)
                else:
                    break
            current = current.next
            i += 1
        
        return head
