from pyparsing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        sum_in_range = 0

        if low <= root.val <= high:
            sum_in_range += root.val

        if root.left is not None:
            sum_in_range += self.rangeSumBST(root.left, low, high)

        if root.right is not None:
            sum_in_range += self.rangeSumBST(root.right, low, high)

        return sum_in_range
        