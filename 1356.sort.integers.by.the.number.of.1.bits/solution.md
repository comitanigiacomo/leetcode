# 1356.sort.integers.by.the.number.of.1.bits 

The program is designed to sort an integer array based on the number of set bits (1s) in their binary representation. If two or more integers have the same number of 1s, they are sorted in ascending order.

Here's the full description of the [problem](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2023-10-30)

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
## Explanation

The sortByBits function takes an integer array `arr` as input and sorts it using the `sort.Slice` function. It defines a custom comparison function as the sorting criterion

The custom comparison function `(func(i, j int) bool)` calculates the number of set bits (1s) for elements at positions i and j in the array arr by calling the countBits function.

The `countBits` function calculates the number of set bits (1s) in the binary representation of an integer n.

Inside the loop, the function uses the bitwise AND operator `(n & 1)` to check the least significant bit of n. If this bit is 1, it increments the count variable.

The function then right-shifts n by one position using `n >>= 1` to check the next bit.


