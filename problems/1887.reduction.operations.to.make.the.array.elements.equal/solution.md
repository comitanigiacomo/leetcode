#  1887.reduction.operations.to.make.the.array.elements.equal

The given problem is to find the minimum number of operations required to make all elements of the array equal

Here's the full description of the [problem](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/?envType=daily-question&envId=2023-11-19)


# Approach 

The approach involves sorting the array in ascending order and then iterating through it. For each unique element encountered, we update the count of operations required to make all subsequent elements equal. The total count is then accumulated and returned.

 
# Complexity 

- **Time complexity**: O(n log n) due to the use of `sort.Ints`
- **Space complexity**: O(1) since the algorithm uses a constant amount of additional space

## Code 

```go
func reductionOperations(nums []int) int {
    sort.Ints(nums)
    count := 0
    add := 0
    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            add++
            count+= add
        }else{
            count+= add
        }

    }
    return count
}
```
