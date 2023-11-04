# 1503.last.moment.before.all.ants.fall.out.of.a.plank


Here's the full description of the [problem](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/?envType=daily-question&envId=2023-11-04)


# Approach

My idea was to not actually consider the change of direction, because this does not represent an additional cost to the problem. For this it is only necessary to find the furthest ant from the end of the table and calculate how many steps it takes to fall



# Complexity

- Time complexity: O(N), where N is the number of ants on one side.
- Space complexity: O(1)


# code

```go
func getLastMoment(n int, left []int, right []int) int {
    leftMax := 0
    rightMax := 0

    if len(left) > 0 {
        leftMax = max(left...)
    }

    if len(right) > 0 {
        rightMax = n - min(right...)
    }

    return max(leftMax, rightMax)
}

func max(nums ...int) int {
    maxNum := nums[0]
    for _, num := range nums {
        if num > maxNum {
            maxNum = num
        }
    }
    return maxNum
}

func min(nums ...int) int {
    minNum := nums[0]
    for _, num := range nums {
        if num < minNum {
            minNum = num
        }
    }
    return minNum
}

```