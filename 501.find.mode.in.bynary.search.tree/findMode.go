/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main

import (
	"fmt"
)

type TreeNode struct {
	Value int
	Left  *TreeNode
	Right *TreeNode
}

func findMode(root *TreeNode) []int {
	var currentElement int
	var currentCount, maxCount int
	var frequentElements []int

	var visit func(node *TreeNode)
	visit = func(node *TreeNode) {
		if node == nil {
			return
		}

		visit(node.Left)

		if node.Value != currentElement {
			currentElement = node.Value
			currentCount = 1
		} else {
			currentCount++
		}

		if currentCount > maxCount {
			maxCount = currentCount
			frequentElements = []int{currentElement} // Reimposta la lista con il nuovo elemento più frequente
		} else if currentCount == maxCount {
			frequentElements = append(frequentElements, currentElement) // Aggiungi l'elemento con lo stesso conteggio massimo
		}

		visit(node.Right)
	}

	visit(root)
	return frequentElements
}

func main() {
	// Esempio di utilizzo
	root := &TreeNode{Value: 1}
	root.Left = nil
	root.Right = &TreeNode{Value: 2}
	root.Right.Left = &TreeNode{Value: 2}

	frequentElements := findMode(root)
	fmt.Println(frequentElements)
}
