from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def recursive(node: TreeNode) -> bool:
            if not node.left and not node.right:  
                return bool(node.val)
            
            left_val = recursive(node.left)
            right_val = recursive(node.right)
            
            if node.val == 2: 
                return left_val or right_val
            elif node.val == 3: 
                return left_val and right_val
            
            return False 

        return recursive(root)

root = [2,1,3,None,None,0,1]
sol = Solution()
print(sol.evaluateTree(root))  
