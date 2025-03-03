class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.summ = 0 
        
        def traverse(node: TreeNode):
            if not node:
                return
            if node.right:
                traverse(node.right)  
            self.summ += node.val
            node.val = self.summ
            if node.left:
                traverse(node.left)  
            
        traverse(root)
        return root
