# 606.construct.string.from.binary.tree

Here's the full description of the [problem](https://leetcode.com/problems/construct-string-from-binary-tree/description/?envType=daily-question&envId=2023-12-08)

# Approach

The approach is to perform a recursive traversal of the binary tree. The base case is when the current node is None, in which case an empty string is returned. For non-empty nodes, the program constructs the string representation considering the left and right subtrees.

# Complexity

- Time complexity: O(n), where `n` is the number of nodes in the binary tree. 
- Space complexity: O(H), where `H` is the height of the tree.

# Code

```Python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"
```