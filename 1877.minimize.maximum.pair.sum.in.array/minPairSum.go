func minPairSum(nums []int) int {
	sort.Ints(nums)
	max := 0

	for i := 0; i < len(nums); i++ {
		if nums[i]+nums[len(nums)-1-i] > max {
			max = nums[i] + nums[len(nums)-1-i]
		}
	}

	return max

}