# 2433. Find the Original Array of Prefix XOR

## Intuition

Efficiently using the XOR operator to deduce information from accumulated data.

Here's the full description of the [problem](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/?envType=daily-question&envId=2023-10-31).

## Approach

- The program starts with the first element of the given `pref` array and uses the XOR operation to calculate the subsequent elements of the `arr` array.
- It initializes an `output` array of the same size as `pref` and set its first element equal to the first element of `pref`.
- Then, it iterates through the `pref` array from index 1 to the end, and at each step, calculates `output[i]` as the XOR of `output[i-1]` and `pref[i]`.

## Complexity

- Time complexity: O(n), where n is the size of the `pref` array.
- Space complexity: O(n), due to the creation of an `output` array of the same size as the `pref` array to store the result.

## Code

```go
func findArray(pref []int) []int {
    output := make([]int, len(pref))
    output[0] = pref[0]
    for i := 1; i < len(pref); i++ {
        output[i] = pref[i-1] ^ pref[i]
    }
    return output
}


