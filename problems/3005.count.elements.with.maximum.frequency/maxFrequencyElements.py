from typing import List
import collections

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = collections.Counter(nums)
        
        max_frequency = max(freq_counter.values())
        
        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]
        
        total_frequency = max_frequency * len(max_freq_elements)
        
        return total_frequency
                
nums = [1,2,3,4,5]
sol1 = Solution()
print(sol1.maxFrequencyElements(nums))
        