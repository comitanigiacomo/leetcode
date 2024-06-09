from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
         # unordered map 'um' implemented
        # as hash table
        um = {}
        n = len(nums)
    
        # 'mod_arr[i]' stores (sum[0..i] % k)
        mod_arr = [0 for i in range(n)]
        max_len = 0
        curr_sum = 0
    
        # Traverse arr[] and build up
        # the array 'mod_arr[]'
        for i in range(n):
            curr_sum += arr[i]
    
            # As the sum can be negative,
            # taking modulo twice
            mod_arr[i] = ((curr_sum % k) + k) % k
    
            # If true then sum(0..i) is
            # divisible by k
            if (mod_arr[i] == 0):
    
                # Update 'max_len'
                max_len = i + 1
    
            # If value 'mod_arr[i]' not present in
            # 'um' then store it in 'um' with index
            # of its first occurrence
            elif (mod_arr[i] not in um):
                um[mod_arr[i]] = i
    
            else:
                # If true, then update 'max_len'
                if (max_len < (i - um[mod_arr[i]])):
                    max_len = i - um[mod_arr[i]]
    
        # Return the required length of longest subarray
        # with sum divisible by 'k'
        return max_len
            
nums = [23, 2, 6, 4, 7]
k = 13
sol1 = Solution()
print(sol1.checkSubarraySum(nums, k)) 
