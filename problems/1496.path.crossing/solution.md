# 1496.path.crossing

Here's the full description of the
[problem](https://leetcode.com/problems/path-crossing/description/?envType=daily-question&envId=2023-12-23)

# Approach

The approach taken in this solution is to use a set to keep track of the visited
points on the path. The current point is represented by a list [x, y]. The
algorithm iterates through the given path, updating the current point based on
the direction of the move (N, S, E, or W). The coordinates of the current point
are added to the set, and if the current point is already in the set, it means
the path has crossed itself, and the algorithm returns True. Otherwise, if the
iteration completes without finding any crossing, it returns False

# Complexity

- Time complexity: O(N), where `N` is the length of the input path
- Space complexity: O(N)

# Code

```Python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        curr = [0,0]
        visited.add(tuple(curr))
        for move in path:
            if move == "N":
                curr[1]+= 1
            elif move == "S":
                curr[1]-= 1
            elif move == "E":
                curr[0] += 1
            else:
                curr[0] -= 1
            print(curr)
            if tuple(curr) not in visited:
                visited.add(tuple(curr))
            else: return True
        return False
```
