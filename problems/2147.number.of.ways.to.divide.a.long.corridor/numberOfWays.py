class Solution:
    def numberOfWays(self, corridor):
        countSeats = 0
        countPlants = 0
        dividers = 1
        mod = 1000000007

        for i in corridor:
            if i == 'S':
                countSeats += 1
            if countSeats == 2 and i == 'P':
                countPlants += 1
            if countSeats == 3:
                dividers *= (countPlants + 1)
                dividers %= mod
                countSeats = 1
                countPlants = 0

        return dividers if countSeats >= 2 else 0
                   
corridor = "SPPSSSSPPS"
sol1 = Solution()
result = sol1.numberOfWays(corridor)
print(result)