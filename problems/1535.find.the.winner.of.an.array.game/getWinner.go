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