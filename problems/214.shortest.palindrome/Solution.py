class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]  # Stringa invertita
        new_s = s + '#' + rev_s
        
        for i in range(len(s)):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s
        return ""

s = "abcd"
sol = Solution()
print(sol.shortestPalindrome(s))
