# 1266.minimum.time.visiting.all.points

Here's the full description of the [problem](https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2023-12-03)

# Intuition

To achieve the goal of reaching the final point in the least possible time, the strategy is to maximize movements in the `2D plane`, particularly by moving horizontally whenever possible.

Moving horizontally in a `2D plane` involves both increasing and decreasing both the `x` and `y` coordinates simultaneously.

Given that the problem requires passing through all points in the order they are provided as input to the program, the objective is to calculate, for each pair of points, the fastest path to move from one point to another.

Now, there are two scenarios for moving from one point to another:

- Move to the point diagonally.
- To reach the point, you need to move either horizontally or vertically at least once.

To address both cases, the algorithm calculates, for each pair of points, the absolute value of the `maximum difference in x or y coordinates`. This allows storing the effective distance for each pair, considering both horizontal and vertical movements.

The algorithm iterates through the list of points, and for each consecutive pair, it computes the `maximum absolute difference` in coordinates (either in x or y). This value is added to the `sum` variable, representing the total minimum time to visit all points.

In summary, the approach aims to maximize horizontal movements, as moving horizontally in a 2D plane involves both `x` and `y` coordinate changes. By calculating the maximum difference in coordinates for each pair of points, the algorithm efficiently determines the minimum time required to traverse the given set of points in the specified order.

# Complexity

- Time complexity: O(N), where `N` is the number of points
- Space complexity: O(1)

## Code

```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sum = 0
        for i in range(1, len(points)):
            sum += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return sum
```