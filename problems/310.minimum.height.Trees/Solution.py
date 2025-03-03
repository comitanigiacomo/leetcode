from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        leaves = [node for node in range(n) if len(adj_list[node]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()  
                adj_list[neighbor].remove(leaf)  
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor) 
            leaves = new_leaves

        return leaves

n = 4
edges = [[1,0],[1,2],[1,3]]
sol = Solution()
print(sol.findMinHeightTrees(n, edges))
