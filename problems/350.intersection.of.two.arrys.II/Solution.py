from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        
        counts = Counter(nums1)
        intersection = []
        for num in nums2:
            if counts[num] > 0:
                intersection.append(num)
                counts[num] -= 1
        return intersection
    
nums1 = nums1 = [1,2,2,1]
nums2 = nums2 = [2,2]    
sol = Solution()
print(sol.intersect(nums1, nums2))