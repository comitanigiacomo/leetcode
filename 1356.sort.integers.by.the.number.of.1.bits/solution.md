# 1356.sort.integers.by.the.number.of.1.bits 

The program is designed to sort an integer array based on the number of set bits (1s) in their binary representation. If two or more integers have the same number of 1s, they are sorted in ascending order.

Here's the full description of the [problem](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2023-10-30)


# Approach


Here's the corrected version with proper spelling:

- The sort.Slice function customizes the sorting of the array.
- The custom sorting function compares two integers, i and j, based on the number of set bits.
- The number of set bits for both arr[i] and arr[j] will be calculated using the countBits function.
- If the number of set bits is the same for both integers (countI == countJ), the program will compare them based on their values (arr[i] < arr[j]), ensuring that elements with the same number of set bits are sorted in ascending order.
- If the number of set bits is different (countI != countJ), the program will compare them based on the number of set bits (countI < countJ), ensuring that elements are sorted by the number of set bits.
The sorted array will be returned as the result.

# Complexity

- Time complexity: O(n * log(n)) (due to the sorting step)
- Space complexity: O(n) (for the input and output arrays)

## Code

```go
func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		countI := countBits(arr[i])
		countJ := countBits(arr[j])

		if countI == countJ {
			return arr[i] < arr[j]
		}

		return countI < countJ
	})
	return arr
}

func countBits(n int) int {
	count := 0
	for n > 0 {
		count += n & 1
		n >>= 1
	}
	return count
}
```