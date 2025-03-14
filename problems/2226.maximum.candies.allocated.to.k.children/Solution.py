from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if sum(candies) < k:
            return 0

        left, right = 1, sum(candies) // k
        best = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)

            if count >= k:
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best
 
candies = [5,8,6]
k = 3
print(Solution().maximumCandies(candies, k))