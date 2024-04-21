from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = deque([source])
        visited = set()
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbour in edges:
                    if neighbour[0] == node or neighbour[1] == node:
                        next_node = neighbour[0] if neighbour[1] == node else neighbour[1]
                        queue.append(next_node)
        
        return False

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
sol1 = Solution()
print(sol1.validPath(n, edges, source, destination))
