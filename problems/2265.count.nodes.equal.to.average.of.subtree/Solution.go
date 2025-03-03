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
