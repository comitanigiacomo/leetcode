func reductionOperations(nums []int) int {
	sort.Ints(nums)
	count := 0
	add := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			add++
			count += add
		} else {
			count += add
		}

	}
	return count
}