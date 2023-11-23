package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{4, 6, 5, 9, 3, 7}
	l := []int{0, 0, 2}
	r := []int{2, 3, 5}
	fmt.Println(checkArithmeticSubarrays(nums, l, r))

}
func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {

	out := []bool{}
	for idx, v := range l {
		arr := []int{}
		arr = append(arr, nums[v:r[idx]+1]...)
		fmt.Println(arr)
		out = append(out, isArithmetic(arr))
	}
	return out
}

func isArithmetic(arr []int) bool {
	sort.Ints(arr)
	var diff int = arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] != diff {
			return false
		}
	}
	return true
}
