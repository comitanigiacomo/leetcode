from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefissi = set()

        for num in arr1:
            while num > 0:
                prefissi.add(num)
                num //= 10

        max_length = 0

        for num in arr2:
            while num > 0:
                if num in prefissi:
                    current_length = len(str(num))

                    max_length = max(max_length, current_length)

                    break
                num //= 10

        return max_length
    
sol = Solution()
arr1 = [1,10,100]
arr2 = [1000]
print(sol.longestCommonPrefix(arr1, arr2))
