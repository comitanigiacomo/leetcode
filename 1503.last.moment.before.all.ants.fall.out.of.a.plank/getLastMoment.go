func getLastMoment(n int, left []int, right []int) int {
	leftMax := 0
	rightMax := 0

	if len(left) > 0 {
		leftMax = max(left...)
	}

	if len(right) > 0 {
		rightMax = n - min(right...)
	}

	return max(leftMax, rightMax)
}

func max(nums ...int) int {
	maxNum := nums[0]
	for _, num := range nums {
		if num > maxNum {
			maxNum = num
		}
	}
	return maxNum
}

func min(nums ...int) int {
	minNum := nums[0]
	for _, num := range nums {
		if num < minNum {
			minNum = num
		}
	}
	return minNum
}