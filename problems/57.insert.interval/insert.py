from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        count = 0
        
        while count < len(intervals) and intervals[count][1] < newInterval[0]:
            new.append(intervals[count])
            count += 1
            
        while count < len(intervals) and intervals[count][0] <= newInterval[1]: 
            newInterval = [min(newInterval[0], intervals[count][0]), max(newInterval[1], intervals[count][1])]
            count += 1
            
        new.append(newInterval)
        new.extend(intervals[count:])
        
        return new
      
intervals = [[1,3],[6,9]]
newInterval = [2,5]
sol1 = Solution()
print(sol1.insert(intervals,newInterval))
        