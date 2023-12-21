# 1637.widest.vertical.area.between.two.points.containing.no.points  

Here's the full description of the [problem](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/?envType=daily-question&envId=2023-12-21)

# Approach

My idea was to sort the points in increasing order based on their x-coordinates and then find the maximum difference between consecutive x-coordinates

# Complexity

- Time complexity: O(n log n), where `n` is the number of points
- Space complexity: O(1)

# Code 

```Python
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max = 0
        for i in range(len(points)-1):
            if points[i+1][0]- points[i][0] > max :
                max = points[i+1][0]- points[i][0] 
        print(max)
        return max
```
