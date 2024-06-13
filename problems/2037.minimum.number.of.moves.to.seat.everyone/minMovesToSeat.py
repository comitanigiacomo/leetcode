from typing import List 

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(h1 - h2) for h1, h2 in zip(sorted(seats), sorted(students))) 

seats = [3,1,5]
students = [2,7,4]
sol = Solution()
print(sol.minMovesToSeat(seats, students))
