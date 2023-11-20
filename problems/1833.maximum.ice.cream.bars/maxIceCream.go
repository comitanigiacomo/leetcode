func maxIceCream(costs []int, coins int) int {

	costs = countingSort(costs)
	count := 0

	for _, v := range costs {
		if coins-v >= 0 {
			coins -= v
			count++
		}
	}
	return count
}

func countingSort(arr []int) []int {
	if len(arr) == 0 {
		return arr
	}

	maxVal := arr[0]
	minVal := arr[0]
	for _, val := range arr {
		if val > maxVal {
			maxVal = val
		}
		if val < minVal {
			minVal = val
		}
	}

	countSize := maxVal - minVal + 1

	count := make([]int, countSize)
	for _, val := range arr {
		count[val-minVal]++
	}

	sortedArr := make([]int, 0, len(arr))
	for i := 0; i < countSize; i++ {
		for count[i] > 0 {
			sortedArr = append(sortedArr, i+minVal)
			count[i]--
		}
	}

	return sortedArr
}