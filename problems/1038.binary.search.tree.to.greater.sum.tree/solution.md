Here's the full description of the [problem](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/)

# Intuition

In this problem, I need to leverage the fact that the tree is a Binary Search Tree (BST). Therefore, I decided to solve the problem using a recursive traversal that takes advantage of its properties.

Specifically, for each node, all the nodes in the tree that have a greater value than it are either the root or nodes in its right subtree, including those on the same level.

# Approach

I performed a post-order recursive traversal on the tree, starting from the largest value. Subsequently, using recursion, I iterate over the nodes at higher levels, incrementing their values accordingly.

# Complexity

- Time complexity: 𝑂(𝑛) where 𝑛 is the number of nodes in the tree.

- Space complexity: 𝑂(ℎ) where ℎ is the height of the tree.

# Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.summ = 0 
        
        def traverse(node: TreeNode):
            if not node:
                return
            if node.right:
                traverse(node.right)  
            self.summ += node.val
            node.val = self.summ
            if node.left:
                traverse(node.left)  
            
        traverse(root)
        return root
```