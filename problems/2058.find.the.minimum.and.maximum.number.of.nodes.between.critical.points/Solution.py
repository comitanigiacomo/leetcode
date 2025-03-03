from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cp = []
        count = 1
        while head and head.next and head.next.next:
            if head.val > head.next.val and head.next.val < head.next.next.val: 
                cp.append(count)
            elif head.val < head.next.val and head.next.val > head.next.next.val: 
                cp.append(count)
            count += 1
            head = head.next
                
        if len(cp) <= 1: return [-1, -1]
        min_so_far = 100000
        for i in range(len(cp)-1):
            min_so_far = min(min_so_far, cp[i+1] - cp[i])
        return [min_so_far, cp[len(cp)-1]- cp[0]]
                    
            
        