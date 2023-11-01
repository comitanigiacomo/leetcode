# 501.find.mode.in.binary.search.tree 

In this problem I have to traverse a binary search tree in order to find the most frequent items (modes)

Here's the full description of the [problem](https://leetcode.com/problems/find-mode-in-binary-search-tree/?envType=daily-question&envId=2023-11-01)


# Approach 1

To determine the mode (the most frequently occurring element) in a binary search tree (BST) with duplicates, I use a depth-first search (DFS) approach. The program traverses the BST while maintaining a "mode" map to track the frequency of each element. The count for each encountered element is incremented during the DFS traversal. After completing the traversal of the entire tree, the program identifies the element(s) with the highest frequency (the mode) and returns them in any order



# Complexity 1

- **Time complexity**: The time complexity of this algorithm is O(n), where n is the number of nodes in the binary search tree. This is because we perform a DFS traversal of the entire tree, visiting each node once.
- **Space complexity**: The space complexity is O(n) as well, as I use the mode map to store the frequency of elements, and in the worst case, it can contain all unique elements in the tree. 

## Code 1

```go
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

func search(node *TreeNode, mode map[int]int) {
	if node.Left != nil {
		search(node.Left, mode)
	}
	if node.Right != nil {
		search(node.Right, mode)
	}
	mode[node.Val]++
}
```

# Intuition

At this point, to improve the program I thought it would be better to try using the BTS without the aid of an auxiliary structure. This results in a reduction in program execution time, as it is no longer necessary to loop through the map


# Approach 2

The program performs an in-order traversal of the BST while maintaining awareness of the current element and its count.
If the program encounters a new element, it resets the current element and count.
Whenever the program finds an element with a count greater than the max count, it updates the max count and resets the frequentElements slice.
If the program encounters an element with the same count as the max count, it adds it to the frequentElements slice.

# Complexity 2

- **Time complexity**: The time complexity of this algorithm is O(n), where "n" is the number of nodes in the binary tree. This is because the program visits each node exactly once during the in-order traversal.

- **Space complexity**: The space complexity is O(h), where "h" is the height of the tree. This is due to the use of recursive calls and the call stack for in-order traversal.

# Code 2


```go
func findMode(root *TreeNode) []int {
	varfunc findMode(root *TreeNode) []int {
	var currentElement int
	var currentCount, maxCount int
	var frequentElements []int

	var visit func(node *TreeNode)
	visit = func(node *TreeNode) {
		if node == nil {
			return
		}
	    visit(root)
	    return frequentElements
    }    
    currentElement int
	var currentCount, maxCount int
	var frequentElements []int

	var visit func(node *TreeNode)
	visit = func(node *TreeNode) {
		if node == nil {
			return
		}

		visit(node.Left)

		if node.Val != currentElement {
			currentElement = node.Val
			currentCount = 1
		} else {
			currentCount++
		}

		if currentCount > maxCount {
			maxCount = currentCount
			frequentElements = []int{currentElement}
		} else if currentCount == maxCount {
			frequentElements = append(frequentElements, currentElement)
		}

		visit(node.Right)
	}

	visit(root)
	return frequentElements
}
```