from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        # Binary search for the maximum minimum distance
        def is_feasible(distance):
            count, last_position = 1, position[0]
            for pos in position[1:]:
                if pos - last_position >= distance:
                    count += 1
                    last_position = pos
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        best_distance = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if is_feasible(mid):
                best_distance = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best_distance

position = [1, 2, 3, 4, 7]
m = 3
sol = Solution()
print(sol.maxDistance(position, m))