# 1609.even.odd.tree

Here's the full description of the [problem](https://leetcode.com/problems/even-odd-tree/description/?envType=daily-question&envId=2024-02-29)

# Approach

The program traverses the tree level by level, keeping track of the current level. At each level, it verifies whether the values in that level satisfy the given conditions and ensure that the values in adjacent nodes follow the appropriate order based on the level's parity.

# Complexity

- Time complexity: O(n) where `n` is the number of nodes in the tree

- Space complexity:O(n)

# Code

```Python
from pyparsing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodi = [root]
        level = 0
        while nodi:
            next_nodi = []
            prev_val = None
            for node in nodi:
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev_val is not None and node.val <= prev_val:
                        return False
                else:
                    if node.val % 2 != 0:
                        return False
                    if prev_val is not None and node.val >= prev_val:
                        return False
                prev_val = node.val
                if node.left:
                    next_nodi.append(node.left)
                if node.right:
                    next_nodi.append(node.right)
            if not next_nodi:
                return True
            nodi = next_nodi
            level += 1
        return -1
```