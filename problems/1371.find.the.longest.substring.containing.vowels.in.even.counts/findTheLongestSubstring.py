class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        state_index_map = {0: -1}  # Lo stato 0 all'inizio (nessuna vocale pari)
        
        current_state = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                current_state ^= vowel_to_bit[char]
            
            if current_state in state_index_map:
                max_length = max(max_length, i - state_index_map[current_state])
            else:
                state_index_map[current_state] = i
        
        return max_length

s = "eleetminicoworoep"
sol = Solution()
print(sol.findTheLongestSubstring(s))