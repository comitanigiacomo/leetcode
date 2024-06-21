from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfied = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            
            if i >= minutes and grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        return base_satisfied + max_additional_satisfied 
                

             
            
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
sol = Solution()
print(sol.maxSatisfied(customers, grumpy, minutes))