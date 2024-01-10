# 2385.amount.of.time.for.binary.tree.to.be.infected

here's the full description of the [problem](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/?envType=daily-question&envId=2024-01-10)

# Approach 

The code uses BFS to simulate the spread of infection through the binary tree.
It initializes a defaultdict (`adjacency_map`) to store the adjacency information for each node, representing the nodes that are adjacent to the current node.
The convert function is used to populate the `adjacency_map` with the adjacent nodes for each node.
The `amountOfTime` function performs `BFS`, updating the set of visited nodes and incrementing the minute count until the entire tree is infected.
The result is the total minutes needed for the entire tree to be infected.

# Complexity

T- Time Complexity: O(N), where `N` is the number of nodes in the binary tree.
- Space Complexity: O(N), as additional space is used for the `deque`, `set`, and `adjacency_map`.

# Code 

```Python
from collections import deque, defaultdict

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root, start):
        map = defaultdict(set)
        self.convert(root, 0, map)
        q = deque()
        q.append(start)
        minute = 0
        visited = set()
        visited.add(start)

        while q:
            level_size = len(q)
            while level_size > 0:
                current = q.popleft()

                for num in map[current]:
                    if num not in visited:
                        visited.add(num)
                        q.append(num)
                level_size -= 1
            minute += 1
        return minute - 1

    def convert(self, current, parent, map):
        if not current:
            return
        if current.val not in map:
            map[current.val] = set()
        adjacent_list = map[current.val]
        if parent != 0:
            adjacent_list.add(parent)
        if current.left:
            adjacent_list.add(current.left.val)
        if current.right:
            adjacent_list.add(current.right.val)
        self.convert(current.left, current.val, map)
        self.convert(current.right, current.val, map)
```