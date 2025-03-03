package main

import (
	"fmt"
)

func main() {
	nums := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(findDiagonalOrder(nums))
}

func findDiagonalOrder(nums [][]int) []int {

	output := []int{}
	sameDiagonal := [][]int{}
	max := 0

	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums[i]); j++ {
			if i+j > max {
				max = i + j
			}
		}
	}

	for i := 0; i <= max; i++ {
		sameDiagonal = append(sameDiagonal, []int{})
	}

	for row, slice := range nums {
		for column, value := range slice {
			sameDiagonal[row+column] = append(sameDiagonal[row+column], value)
		}
	}

	for _, v := range sameDiagonal {
		for i := len(v) - 1; i >= 0; i-- {
			output = append(output, v[i])
		}
	}
	return output
}
