# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodi = [root]
        while nodi:
            next_nodi = []
            for node in nodi:
                if node.left:
                    next_nodi.append(node.left)
                if node.right:
                    next_nodi.append(node.right)
            if not next_nodi:
                return nodi[0].val
            nodi = next_nodi
        return -1




