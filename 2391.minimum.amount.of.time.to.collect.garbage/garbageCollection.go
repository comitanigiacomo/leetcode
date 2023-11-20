package main

import (
	"fmt"
	"strings"
)

func main() {
	garbage := []string{"G", "P", "GP", "GG"}
	travel := []int{2, 4, 3}
	fmt.Println(garbageCollection(garbage, travel))
}

func garbageCollection(garbage []string, travel []int) int {
	out := 0
	visited := make(map[string]bool)

	for i := len(garbage) - 1; i >= 0; i-- {
		letters := strings.Split(garbage[i], "")
		for _, v := range letters {
			if !visited[v] {
				visited[v] = true
			}
		}
		if i > 0 {
			out += travel[i-1] * len(visited)
		}

		out += len(garbage[i])

	}
	return out
}
