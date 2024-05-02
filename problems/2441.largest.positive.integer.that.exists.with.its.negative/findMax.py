from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max = -1
        for elem in nums:
            if elem > max and -elem in nums_set :
                max = elem
        return max 