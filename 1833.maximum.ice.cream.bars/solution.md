# 1833 Maximum Ice Cream Bars 


Here's the full description of the [problem](https://leetcode.com/problems/maximum-ice-cream-bars/description/)


# Approach

The central idea of ​​the program is to use counting sort to sort the costs array in ascending order, then scan it and count the number of bars that can be taken before running out of coins

The counting array is sized based on the range of values in the input array. Counts are stored based on the actual value minus the minimum value to avoid empty spaces in the counting array.


# Complexity

- Time complexity: O(n)

The counting sort has a time complexity of O(n) to sort the costs array efficiently, where n is the number of ice cream bars.
The subsequent iteration through the sorted array also takes O(n) time.
- Space complexity: O(n)
The program uses additional space for the sorted array in the counting sort, which takes O(n) space.
The space complexity is mainly due to the need to store the input and output arrays.

# code

```go
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
```