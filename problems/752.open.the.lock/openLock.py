from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbors(lock):
            neighbors = []
            for i in range(4):
                for diff in (1, -1):
                    new_digit = (int(lock[i]) + diff) % 10
                    neighbor = lock[:i] + str(new_digit) + lock[i+1:]
                    neighbors.append(neighbor)
            return neighbors
        
        queue = deque([('0000', 0)])
        visited = set(deadends)
        
        while queue:
            lock, moves = queue.popleft()
            if lock == target:
                return moves
            if lock in visited:
                continue
            visited.add(lock)
            for neighbor in get_neighbors(lock):
                if neighbor not in visited:
                    queue.append((neighbor, moves + 1))
        
        return -1

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
sol = Solution()
print(sol.openLock(deadends, target))
