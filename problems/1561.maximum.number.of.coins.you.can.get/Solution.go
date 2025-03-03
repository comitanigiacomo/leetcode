package main

import (
	"fmt"
	"sort"
)

func main() {
	piles := []int{2, 4, 1, 2, 7, 8}
	fmt.Println(maxCoins(piles))

}

func maxCoins(piles []int) int {
	sort.Ints(piles)

	out := 0

	var flag bool

	for i := len(piles) - 1; i >= len(piles)/3; i-- {

		flag = !flag
		if flag == false {
			out += piles[i]
		}
	}
	return out
}
