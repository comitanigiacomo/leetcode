# 2265.count.nodes.equal.to.average.of.subtree

Given a binary tree, count the number of nodes whose label is equal to the average of the labels of the nodes in its subtree

Here's the full description of the [problem](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/?envType=daily-question&envId=2023-11-02)


# Approach

The idea was to create a function that, given a binary tree as input, starting from the root returns the number of nodes present in the subtrees and the sum of their values, in order to calculate the average value. After that I created a separate function that applies the one just described for each node, and counts those that have value equal to the calculated average value

# Complexity

- Time complexity: O(N), where N is the number of nodes in the tree.
- Space complexity: O(H), where H is the height of the tree

# code

```go
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfSubtree(root *TreeNode) int {
	count := 0
	if root == nil {
		return 0
	}

	subTreeSize, subTreeSum := average(root)

	if root.Val == subTreeSum/subTreeSize {
		count++
	}

	leftCount := averageOfSubtree(root.Left)
	rightCount := averageOfSubtree(root.Right)

	count += leftCount + rightCount

	return count
}

func average(node *TreeNode) (int, int) {
	if node == nil {
		return 0, 0
	}

	leftSize, leftSum := average(node.Left)
	rightSize, rightSum := average(node.Right)

	subtreeSize := 1 + leftSize + rightSize
	subtreeSum := node.Val + leftSum + rightSum

	return subtreeSize, subtreeSum
}

```