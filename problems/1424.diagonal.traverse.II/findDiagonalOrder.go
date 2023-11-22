package main

import (
	"fmt"
)

func main() {
	nums := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(findDiagonalOrder(nums))
}

func findDiagonalOrder(nums [][]int) []int {

	final := []int{}
	arr := [][]int{}
	max := 0

	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums[i]); j++ {
			if i+j > max {
				max = i + j
			}
		}
	}

	for i := 0; i <= max; i++ {
		arr = append(arr, []int{})
	}

	for row, slice := range nums {
		for column, value := range slice {
			arr[row+column] = append(arr[row+column], value)
		}
	}

	for _, v := range arr {
		for i := len(v) - 1; i >= 0; i-- {
			final = append(final, v[i])
		}
	}

	return final

}
