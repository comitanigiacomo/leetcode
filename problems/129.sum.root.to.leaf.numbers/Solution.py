from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        total_sum = 0
        queue = [(root, 0)]
        
        while queue:
            node, current_sum = queue.pop(0)
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                total_sum += current_sum
            
            if node.left:
                queue.append((node.left, current_sum))
            if node.right:
                queue.append((node.right, current_sum))
        
        return total_sum