from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1 for _ in range(n)] for _ in range m]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        row,col = 0, 0
        
        curr = head
        
        top,bottom,left,right = 0, m -1, 0, n-1
        
        while curr: 
            matrix[row][col] = curr.val
            
            curr = curr.next  
            
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
            
            if not (top <= next_row <= bottom and left <= next_col <= right):

                if direction_idx == 0:  # destra
                    top += 1
                elif direction_idx == 1:  # giù
                    right -= 1
                elif direction_idx == 2:  # sinistra
                    bottom -= 1
                else:  # su
                    left += 1
                
                direction_idx = (direction_idx + 1) % 4
                
            row += directions[direction_idx][0]
            col += directions[direction_idx][1]
        
        return matrix
            
        