# 935.knight.dialer

Here's the full description of the [problem](https://leetcode.com/problems/knight-dialer/description/?envType=daily-question&envId=2023-11-27)


# Approach

The problem is essentially asking for the number of distinct phone numbers of length n that can be dialed using a knight on a phone dialer. The idea here is to simulate the knight's moves on the dialer for n-1 jumps and count the possibilities.

The code uses dynamic programming to store the number of ways to reach each digit after each jump. The cur_pos array is updated for each jump, and the result is the sum of the values in the final cur_pos array.

# Complexity

- Time complexity: O(n)
- Space complexity: O(1)

## Code

```python
class Solution:
    mod = 10**9 + 7 
    def knightDialer(self, n: int) -> int:
        cur_pos = [1]* 10
        for jump in range (2, n +1):
            new_pos = [0]*10
            
            new_pos[0] = (cur_pos[6] + cur_pos[4]) % self.mod
            new_pos[1] = (cur_pos[6] + cur_pos[8]) % self.mod
            new_pos[2] = (cur_pos[7] + cur_pos[9]) % self.mod
            new_pos[3] = (cur_pos[4] + cur_pos[8]) % self.mod
            new_pos[4] = (cur_pos[0] + cur_pos[3] + cur_pos[9]) % self.mod
            new_pos[6] = (cur_pos[0] + cur_pos[1] + cur_pos[7]) % self.mod
            new_pos[7] = (cur_pos[2] + cur_pos[6]) % self.mod
            new_pos[8] = (cur_pos[1] + cur_pos[3]) % self.mod
            new_pos[9] = (cur_pos[2] + cur_pos[4]) % self.mod

            cur_pos = new_pos 

        total_count = sum(cur_pos) % self.mod
        return total_count
```