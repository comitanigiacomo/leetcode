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

path ="NESWW"
sol1 = Solution()
result = sol1.isPathCrossing(path)
print(result)




