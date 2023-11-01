/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// first idea: I create an auxiliary structure to keep track of the number of times
// each node is present in the tree, and return the most frequent ones
func findMode(root *TreeNode) []int {
	mode := make(map[int]int)

	search(root, mode)

	var max int

	var modes []int

	for _, v := range mode {
		if v > max {
			max = v
		}
	}

	for k, v := range mode {
		if v == max {
			modes = append(modes, k)
		}
	}

	return modes

}

// recursive function that visits the tree in post order
func search(node *TreeNode, mode map[int]int) {
	if node.Left != nil {
		search(node.Left, mode)
	}
	if node.Right != nil {
		search(node.Right, mode)
	}
	mode[node.Val]++
}