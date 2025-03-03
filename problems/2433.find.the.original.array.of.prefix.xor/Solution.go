package main

import "fmt"

func main() {
	arr := []int{13}
	fmt.Println(findArray(arr))

}

func findArray(pref []int) []int {
	output := make([]int, len(pref))
	output[0] = pref[0]
	for i := 1; i < len(pref); i++ {
		output[i] = pref[i-1] ^ pref[i]
	}
	return output
}
