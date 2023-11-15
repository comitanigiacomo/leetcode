# 1846.maximum.element.after.decreasing.and.rearranging

Here's the full description of the [problem](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/?envType=daily-question&envId=2023-11-15)


# Approach

1. Sort the input array in ascending order.
2. Set the first element of the sorted array to 1, ensuring the minimum value.
3. Iterate through the array starting from the second element.
4. For each element, check if the absolute difference between the current element and the previous element is greater than 1.
5. If the difference is greater than 1, update the current element to be one more than the previous element.

# Complexity

- Time complexity: O(n log n) due to the sorting operation
- Space complexity: O(1) : The algorithm sorts the array in-place, and the additional space used is constant


# code


```go
func maximumElementAfterDecrementingAndRearranging(arr []int) int {
    sort.Ints(arr)
    arr[0] = 1
    for i := 1; i < len(arr); i++ {
        if math.Abs(float64(arr[i] - arr[i-1])) > 1 {
            arr[i] = arr[i-1]+1
        }

    }
    return arr[len(arr)-1]
}
```