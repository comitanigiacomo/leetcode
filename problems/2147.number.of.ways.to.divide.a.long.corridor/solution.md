# 2147.number.of.ways.to.divide.a.long.corridor

Here's the full description of the [problem](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2023-11-28)

# Approach 

The program Iterates through the `corridor` string, and for each character:

If it is 'S', increment the `countSeats` variable.
If `countSeats` becomes 2 and the character is 'P', increment the `countPlants`variable.
If `countSeats` becomes 3, update the `dividers` by multiplying it with `(countPlants + 1)` and take the modulo with `mod`. Reset `countSeats` to 1 and `countPlants` to 0.
Finally, return `dividers` if `countSeats` is greater than or equal to 2; otherwise, return 0.

 
# Complexity 

- **Time complexity**: O(n) where `n` is the length of `corridor`
- **Space complexity**: O(1)

# code

```python
class Solution:
    def numberOfWays(self, corridor):
        countSeats = 0
        countPlants = 0
        dividers = 1
        mod = 1000000007

        for i in corridor:
            if i == 'S':
                countSeats += 1
            if countSeats == 2 and i == 'P':
                countPlants += 1
            if countSeats == 3:
                dividers *= (countPlants + 1)
                dividers %= mod
                countSeats = 1
                countPlants = 0

        return dividers if countSeats >= 2 else 0
```