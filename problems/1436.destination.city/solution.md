# 1436.destination.city

Here's the full descritpion of the [problem](https://leetcode.com/problems/destination-city/description/?envType=daily-question&envId=2023-12-15)

# Approach

To solve this, I thought of keeping track of all starting cities and then iterate through the paths to find the destination city.

# Complexity

- Time complexity: O(N), where N is the number of paths
- Space complexity: O(N)

# Code

```Python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()

        for path in paths:
            cities.add(path[0])

        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest 
        return ""
```


