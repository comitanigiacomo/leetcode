# 1838.frequency.of.the.most.frequent.element

The goal of this problem is to find the maximum frequency of an element in the given integer array `nums` after performing at most `k` operations.

Here's the full description of the [problem](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/?envType=daily-question&envId=2023-11-18)


# Approach 

The provided code implements a sliding window approach to efficiently find the maximum frequency. The `left` and `right` pointers define the window, and the `sum` variable keeps track of the sum of elements in the window. The inner loop adjusts the window size to satisfy the condition `nums[right]*(right-left+1) <= sum+k`. The `max` function is a simple utility function to find the maximum of two integers.
 
# Complexity 

- Time Complexity: O(n log n) due to the sorting step.
- Space Complexity: O(1)

## Code 

```go
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
```
