from collections import defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Costruisci la lista di adiacenza
        graph = defaultdict(list)
        for src, dst in edges:
            graph[dst].append(src)
        
        # Funzione per fare DFS e trovare gli antenati
        def dfs(node, visited):
            if node in visited:
                return visited[node]
            ancestors = set()
            for parent in graph[node]:
                ancestors.add(parent)
                ancestors.update(dfs(parent, visited))
            visited[node] = ancestors
            return ancestors
        
        visited = {}
        result = []
        for i in range(n):
            ancestors = dfs(i, visited)
            result.append(sorted(ancestors))
        
        return result

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
sol = Solution()
print(sol.getAncestors(n, edgeList))
