# 94.binary.tree.inorder.trasversal

Here's the full description of the [problem](https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=daily-question&envId=2023-12-09)

# Approach

The approach used in the program is a recursive inorder traversal. The inorder traversal visits the nodes in the order left subtree, root, right subtree. The base case is when the current node is None, and in that case, no values are added to the result. Otherwise, it recursively traverses the left subtree, adds the value

# Complexity

- Time complexity: O(N), where N is the number of nodes in the binary tree.
- Space complexity: O(H), where H is the height of the binary tree

# Code

```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result += self.inorderTraversal(root.left)
 
            result.append(root.val)
 
            result += self.inorderTraversal(root.right)
        
        return result
```
