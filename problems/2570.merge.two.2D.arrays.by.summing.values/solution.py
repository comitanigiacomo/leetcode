from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        
        return result
    
nums1 = [[1, 3], [2, 5], [3, 7]]
nums2 = [[1, 5], [2, 5], [3, 5], [4, 5]]
print(Solution().mergeArrays(nums1,nums2))