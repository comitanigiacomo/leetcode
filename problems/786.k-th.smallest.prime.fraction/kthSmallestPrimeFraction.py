from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = {}
        for i in range (len(arr)):
            for j in range (len(arr)):
                if 0 <= i < j < len(arr):
                    fractions[arr[i]/arr[j]] = arr[i], arr[j]
        sorted_fractions = sorted(fractions.keys())
        return fractions[sorted_fractions[k-1]]
        
arr = [1,2,3,5]
k = 3
sol1 = Solution()
print(sol1.kthSmallestPrimeFraction(arr,k))