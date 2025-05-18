
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []

        def backtracking(current: TreeNode, path: List[str]):
            if not current.left and not current.right:
                result.append("->".join(path))
                return

            if current.right:
                backtracking(current.right, path + [str(current.right.val)])

            if current.left:
                backtracking(current.left, path + [str(current.left.val)])

        if root:
            backtracking(root, [str(root.val)])

        return result

