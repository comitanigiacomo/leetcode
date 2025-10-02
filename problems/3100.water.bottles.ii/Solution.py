class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        drunk , empty = 0, 0
        
        def bevi(n: int):
            nonlocal drunk, empty, numBottles
            drunk += numBottles
            empty += numBottles
            numBottles = 0

        bevi(numBottles)
        
        while empty >= numExchange:
            
            empty -= numExchange
            numExchange += 1
            numBottles += 1
            
            if empty < numExchange:
                if empty + numBottles >= numExchange:
                    bevi(numBottles)
           
        return drunk + numBottles
    
numBottles = 10
numExchange = 3
    
sol = Solution()
print(sol.maxBottlesDrunk(numBottles, numExchange))