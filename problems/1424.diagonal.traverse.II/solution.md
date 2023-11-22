# 1424.diagonal.traverse.II

Here's the full description of the [problem](https://leetcode.com/problems/diagonal-traverse-ii/description/?envType=daily-question&envId=2023-11-22)


# Approach

- Iterate through the nums array to find the maximum diagonal index (max).
- Create a 2D slice `sameDiagonal` to store elements from the same diagonal.
- Populate the `sameDiagonal` slice with elements from nums.
- Traverse the `sameDiagonal` slice in reverse order and append elements to the `output` slice.

# Complexity

- Time complexity: O(N + M), where N is the total number of elements in nums and M is the maximum diagonal index.
- Space complexity:O(N)

# code

```go
func findDiagonalOrder(nums [][]int) []int {

	output := []int{}
	sameDiagonal := [][]int{}
	max := 0

	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums[i]); j++ {
			if i+j > max {
				max = i + j
			}
		}
	}

	for i := 0; i <= max; i++ {
		sameDiagonal = append(sameDiagonal, []int{})
	}

	for row, slice := range nums {
		for column, value := range slice {
			sameDiagonal[row+column] = append(sameDiagonal[row+column], value)
		}
	}

	for _, v := range sameDiagonal {
		for i := len(v) - 1; i >= 0; i-- {
			output = append(output, v[i])
		}
	}
	return output
}
```