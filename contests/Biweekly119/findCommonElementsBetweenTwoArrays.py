from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [0,0]
        for idx,elem in enumerate(nums1):
            if elem in nums2:
                out[0] += 1
        for idx,elem in enumerate(nums2):
            if elem in nums1:
                out[1] += 1
        return out  
