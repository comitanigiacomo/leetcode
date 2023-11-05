#  1535.find.the.winner.of.an.array.game

The program solves the problem of finding the winner of a game where two distinct integers compete in consecutive rounds. The game continues until one of them wins k consecutive rounds. 

Here's the full description of the [problem](eetcode.com/problems/find-the-winner-of-an-array-game/?envType=daily-question&envId=2023-11-05)


# Approach 

If k is greater than or equal to the length of the array, then the program returns the maximum element of the array. Otherwise, it scans the array where it compares the current element to the maximum element each time, and keeps track of the number of wins. When the element currently considered maximum has a number of victories equal to k, the program ends
 
# Complexity 

- **Time complexity**: O(n), where n is the length of the array
- **Space complexity**: O(1)

## Code 

```go
    func getWinner(arr []int, k int) int {
	n := len(arr)
	if k >= n-1 {
		maxVal := arr[0]
		for i := 1; i < n; i++ {
			if arr[i] > maxVal {
				maxVal = arr[i]
			}
		}
		return maxVal
	}

	currentMax := arr[0]
	consecutiveWins := 0

	for i := 1; i < n; i++ {
		if arr[i] > currentMax {
			currentMax = arr[i]
			consecutiveWins = 1
		} else {
			consecutiveWins++
		}

		if consecutiveWins == k {
			return currentMax
		}
	}

	return currentMax
}
```
