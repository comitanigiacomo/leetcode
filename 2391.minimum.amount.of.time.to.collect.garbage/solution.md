# 2391.minimum.amount.of.time.to.collect.garbage

Here's the full description of the [problem](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/solutions/?envType=daily-question&envId=2023-11-20)


# Approach

The algorithm iterates through the garbage locations in reverse order. For each location, it keeps track of the types of garbage encountered so far using a map (visited). It calculates the time required to travel from the current location to the previous one, multiplied by the number of distinct types of garbage encountered. Additionally, it adds the length of the current garbage location to the total time.


# Complexity

Time complexity: O(N * M), where N is the number of garbage locations and M is the average length of a garbage location.

Space complexity: O(K), where K is the total number of distinct types of garbage across all locations.


# code

```go
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
```
