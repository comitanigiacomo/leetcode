from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #Converto i numeri in stringhe per confrontarli
        nums_str = list(map(str, nums))
                
        # Ordino in base alla prima cifra, poi alla seconda...
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Unisco i numeri ordinati in una singola stringa
        result = ''.join(nums_str)
        
        # Se il risultato è tutti 0 restituisco 0.
        return '0' if result[0] == '0' else result

nums = [3,30,34,5,9]
sol = Solution()
print(sol.largestNumber(nums))