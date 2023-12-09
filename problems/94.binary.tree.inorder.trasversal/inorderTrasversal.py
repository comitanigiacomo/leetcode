from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            # First recur on left child
            result += self.inorderTraversal(root.left)
 
            # Then append the data of node
            result.append(root.val)
 
            # Now recur on right child
            result += self.inorderTraversal(root.right)
        
        return result

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
sol1 = Solution()
result = sol1.inorderTraversal(root)
print(result)