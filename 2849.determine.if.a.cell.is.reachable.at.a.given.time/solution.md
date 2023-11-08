# 2849.determine.if.a.cell.is.reachable.at.a.given.time

The program establishes whether it is possible to get from a starting cell to a finishing cell, moving in a 2D grid for t steps.

Here's the full description of the [problem](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)


# Approach

My idea was to calculate the minimum path to go from the `(sx,sy)` cell to the `(fx,fy)` cell, and compare it with the given value `t`. In fact, if the `t` value is greater than or equal to the shortest path, then it is possible to reach the `(fx,fy)` cell. To calculate the shortest path, the program only considers the minimum value between the distances of the point coordinates. This is to consider cases in which it is possible to move diagonally between adjacent cells.

It is important to note that if the `(sx,sy)` and `(fx,fy)` cells coincide, the value of `t` must be different from 1


# Complexity

- Time complexity: O(1)
- Space complexity: O(1)

## Code

```go
func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
    distX := abs(fx-sx)
    distY :=  abs(fy-sy)
    pMin := 0
    if sx == fx && sy == fy {
        if t != 1 {
            return true
        }
    }else{
        pMin = max(distX, distY)
        if t >= pMin {
            return true
        }
    }
    return false
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func max(x,y int )int {
    if x > y {
        return x
    }
    return y
}

```