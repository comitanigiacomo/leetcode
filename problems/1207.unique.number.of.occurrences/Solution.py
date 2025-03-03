from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        frequency = {}
        freqOfSet = set()
    
        for i in arr:
            frequency[i] = frequency.get(i, 0) + 1
    
        for f in frequency.values():
            freqOfSet.add(f)
    
        return len(freqOfSet) == len(frequency)         
        
arr = [1,2,2,1,1,3]
sol1 = Solution()
print(sol1.uniqueOccurrences(arr))