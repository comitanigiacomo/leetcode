func maxFrequency(nums []int, k int) int {
	sort.Ints(nums)
	maxFreq := 0
	left := 0
	sum := 0

	for right := 0; right < len(nums); right++ {
		sum += nums[right]

		for nums[right]*(right-left+1) > sum+k {
			sum -= nums[left]
			left++
		}

		maxFreq = max(maxFreq, right-left+1)
	}

	return maxFreq
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}