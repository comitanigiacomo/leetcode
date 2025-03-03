from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        part_size = length // k  
        extra = length % k

        ans = []
        curr = head
        for i in range(k):
            part_head = curr  
            part_length = part_size + (1 if i < extra else 0)  
            
            for j in range(part_length - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None  
                curr = next_part  
            ans.append(part_head)

        while len(ans) < k:
            ans.append(None)

        return ans