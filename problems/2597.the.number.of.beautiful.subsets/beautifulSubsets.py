from typing import List

class Solution:
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        mod_map = defaultdict(int)
        
        def backtrack(index):
            if index == len(nums):
                return 1
            
            num = nums[index]

            add_conflict = num + k
            sub_conflict = num - k
            total_count = 0
            
            total_count += backtrack(index + 1)
            
            if mod_map[add_conflict] == 0 and mod_map[sub_conflict] == 0:
                mod_map[num] += 1
                total_count += backtrack(index + 1)
                mod_map[num] -= 1
            
            return total_count
        
        return backtrack(0) - 1

nums = [2, 4, 6]
k = 2
sol1 = Solution()
print(sol1.beautifulSubsets(nums, k))
