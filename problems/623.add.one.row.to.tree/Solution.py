from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Creo un albero avente come radice il nuovo nodeo, e il vecchio nodo come nodo sinistro della radice
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        # Caso base 
        if depth == 2:
            leftNode = TreeNode(val)
            leftNode.left = root.left
            root.left = leftNode
            
            rightNode = TreeNode(val)
            rightNode.right = root.right
            root.right = rightNode
        else:
            if root.left:
                self.addOneRow(root.left, val, depth - 1)
            if root.right:
                self.addOneRow(root.right, val, depth - 1)
        
        return root