package main

import (
	"fmt"
	"sort"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8}
	fmt.Println(sortByBits(arr))
}

func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		countI := countBits(arr[i])
		countJ := countBits(arr[j])

		if countI == countJ {
			return arr[i] < arr[j]
		}

		return countI < countJ
	})
	return arr
}

func countBits(n int) int {
	count := 0
	for n > 0 {
		count += n & 1
		n >>= 1
	}
	return count
}
