from collections import Optional, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        
        self.values = set()
        if root:
            self.recover_tree(root, 0)
            
    def recover_tree(self, node: Optional[TreeNode], value: int):
        if not node:
            return
        node.val = value
        self.values.add(value)
        self.recover_tree(node.left, 2 * node.val + 1)
        self.recover_tree(node.right, 2 * node.val + 2)
                
    def find(self, target: int) -> bool:
        return target in self.values