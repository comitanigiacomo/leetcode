class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        str1 = s[:len(s)// 2]
        str2 = s [len(s)//2:]
        vowels1 = [str1.count(x) for x in "aeiouAEIOU"]
        vowels2 = [str2.count(x) for x in "aeiouAEIOU"]
    
        return sum(vowels1) == sum(vowels2)
        
input = "textbook"
sol1 = Solution()
print(sol1.halvesAreAlike(input)) 