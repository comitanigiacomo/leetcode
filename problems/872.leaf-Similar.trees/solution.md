# 872.leaf-Similar.trees

Here's the full description of the [problem](https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-01-09)

# Approach

The approach involves performing a depth-first traversal on both trees and collecting the leaf values in order. The leaf values are then compared to check if the two trees are leaf-similar.

# Complexity

- Time complexity: O(N), where `N` is the total number of nodes in the trees.
- Space complexity: O(H), where `H` is the height of the trees

# Code 

```Python
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if node:
                if not node.left and not node.right:
                    leaves.append(node.val)
                dfs(node.left, leaves)
                dfs(node.right, leaves)

        leaves1, leaves2 = [], []
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
        
```