from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)  # Trova il valore massimo nell'array
        max_len = 0
        current_len = 0
        
        for num in nums:
            if num == max_num:
                current_len += 1  # Incrementa la lunghezza del subarray se il numero è il massimo
                max_len = max(max_len, current_len)  # Aggiorna la lunghezza massima del subarray
            else:
                current_len = 0  # Reset della lunghezza se il numero non è il massimo
                
        return max_len
    
nums = [1,2,3,4]
sol = Solution()
print(sol.longestSubarray(nums))