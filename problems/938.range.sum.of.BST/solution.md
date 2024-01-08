# 938.range.sum.of.BST

Here's the full description of the [problem](https://leetcode.com/problems/range-sum-of-bst/description/?envType=daily-question&envId=2024-01-08)

# Approach

The approach to solving this problem is to perform a depth-first traversal of the binary search tree. During the traversal, the program checks whether the value of the current node falls within the specified range [low, high]. If it does, it adds the value to the sum. Then recursively explores the left and right subtrees, applying the same logic.

# Complexity

- Time complexity: O(N), where `N` is the number of nodes in the binary search tree
- Space complexity:  O(H), where `H` is the height of the binary search tree

# code 

```python
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
```