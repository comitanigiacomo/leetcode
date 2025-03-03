from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        minor = []
        greater = []
        equals = []

        for elem in nums:
            if elem < pivot: minor.append(elem)
            elif elem > pivot: greater.append(elem)
            elif elem == pivot: equals.append(elem)

        return minor + equals + greater
        
nums = [9,12,5,10,14,3,10]
pivot = 10
print(Solution().pivotArray(nums, pivot))

# Occhio che in realta sta chiedendo prima parte del quicksort