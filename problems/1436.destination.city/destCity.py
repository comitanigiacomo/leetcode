from typing import List

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
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
sol1 = Solution()
result = sol1.destCity(paths)
print(result)