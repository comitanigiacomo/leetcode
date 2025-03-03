from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedArr = []
        self.inOrderTrasversal(root)
        return self.sortedArrToBST(0, len(self.sortedArr)-1)
    
    def inOrderTrasversal(self, root: TreeNode): 
        if not root: return 
        if root.left : 
            self.inOrderTrasversal(root.left)
        self.sortedArr.append(root)
        if root.right:
            self.inOrderTrasversal(root.right)
    
    def sortedArrToBST(self, start: int, end: int) -> TreeNode: 
        if start > end : return None
        
        mid = (start + end) // 2 
        root = self.sortedArr[mid]
        root.left = self.sortedArrToBST(start, mid - 1)
        root.right = self.sortedArrToBST(mid + 1, end)
        return root 
        