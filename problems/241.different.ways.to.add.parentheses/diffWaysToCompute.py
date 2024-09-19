from typing import List
from collections import Counter

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def eval_expression(exp: str) -> List[int]:
            if exp.isdigit():
                return [int(exp)]
            
            results = []
            for i, char in enumerate(exp):
                if char in "*-+":
                    left_results = eval_expression(exp[:i])
                    right_results = eval_expression(exp[i + 1:])
                    
                    
                    for left in left_results:
                        for right in right_results:
                            if char == "+":
                                results.append(left + right)
                            elif char == "-":
                                results.append(left - right)
                            elif char == "*":
                                results.append(left * right)
            return results
        
        return eval_expression(expression)
    

expression = expression = "2*3-4*5"    
sol = Solution()
print(sol.diffWaysToCompute(expression))
