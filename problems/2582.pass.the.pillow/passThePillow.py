class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        index = 1
        for i in range(time):
            if index == n : 
                direction *= -1
            if index == 1 and direction == -1: 
                direction *= -1
            index += direction
        return index


n = 4
time = 5
sol = Solution()
print(sol.passThePillow(n, time))