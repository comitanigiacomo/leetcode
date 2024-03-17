# 57.insert.interval

Here's the full description of the [problem](https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-03-17)

# Approach

The approach involves iterating through the `intervals` list and comparing each interval with the new interval to determine their relationship and merge them if necessary. We maintain a new list `new` to store the merged intervals. We iterate through the `intervals` list until we find intervals that are strictly before the new interval, then we append them directly to `new`. Next, we merge intervals that overlap with the new interval and update the new interval accordingly. Finally, we append the updated new interval and the remaining intervals to `new`.

# Complexity

- Time complexity: O(n), where `n` is the number of intervals in the given list

- Space complexity: O(n)

# Code

```Python
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
```