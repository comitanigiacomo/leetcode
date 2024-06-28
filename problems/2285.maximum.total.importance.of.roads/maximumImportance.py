from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Initialize the dictionary with default value 0
        my_dict = defaultdict(int)
        for road in roads: 
            my_dict[road[0]] += 1
            my_dict[road[1]] += 1
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
        
        cities_val = {}
        for elem in sorted_dict: 
            cities_val[elem] = n
            n -= 1

        count = 0
        for elem in roads: 
            count += cities_val[elem[0]] + cities_val[elem[1]]
        return count
        
n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
sol = Solution()
print(sol.maximumImportance(n, roads))
