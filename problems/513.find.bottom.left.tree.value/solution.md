# 513.find.bottom.left.tree.value

here's the full description of the [problem](https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28)

# Approach
To find the bottom-left value of a binary tree, we can perform a level order traversal (`BFS`) starting from the root. During traversal, we maintain a list of nodes at each level. After traversing all levels, the leftmost node at the last level will be the bottom-left value of the tree.

# Complexity

- Time complexity: O(n) where `n` is the number of nodes in the tree.

- Space complexity: O(w) where `w` is the maximum width of the tree (number of nodes in the widest level).

# Code 

```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodi = [root]
        while nodi:
            next_nodi = []
            for node in nodi:
                if node.left:
                    next_nodi.append(node.left)
                if node.right:
                    next_nodi.append(node.right)
            if not next_nodi:
                return nodi[0].val
            nodi = next_nodi
        return -1
```