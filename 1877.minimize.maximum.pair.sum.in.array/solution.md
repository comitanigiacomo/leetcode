# 1877.minimize.maximum.pair.sum.in.array

Here's the full description of the [problem](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2023-11-17)


# Approach 

The approach involves sorting the array in ascending order. Then, we pair the smallest element with the largest, the second smallest with the second largest, and so on. We find the maximum sum among these pairs.
 
# Complexity 

- **Time complexity**: O(nlog(n)) - Sorting the array takes O(nlog(n)) time.
- **Space complexity**: O(1) - Constant space is used.

## Code 

```go
func minPairSum(nums []int) int {
    sort.Ints(nums)
    max := 0

    for i := 0; i < len(nums); i++ {
        if nums[i] + nums[len(nums)-1-i] > max {
            max =  nums[i] + nums[len(nums)-1-i]
        }
    }

    return max
    
}
```
