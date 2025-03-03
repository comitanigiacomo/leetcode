# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List 
from typing import Optional 

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        
        left_values = self.postorderTraversal(root.left)
        
        right_values = self.postorderTraversal(root.right)
        
        return left_values + right_values + [root.val]