from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root:
            if root.left: 
                # First recur on left child
                self.removeLeafNodes(root.left, target)
            if root.right:
                # The recur on right child
                self.removeLeafNodes(root.right, target)
            
            # Then visit the node
            if root.left and root.left.val == target and not root.left.left and not root.left.right : root.left = None
            if root.right and root.right.val == target and not root.right.left and not root.right.right: root.right = None
            
            # Finally check if we have to delete root
            if not root.left and not root.right and root.val == target: return None
        return root

            
            
        
        
root = [1,2,3,2,None,2,4]
target = 2
sol1 = Solution
print(sol1.removeLeafNodes(root,target))