class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        
        while numBottles >= numExchange: 
            totalBottles += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
            
        return totalBottles
        
numBottles = 9
numExchange = 3
sol = Solution()
print(sol.numWaterBottles(numBottles, numExchange))