# To solve the problem, I simply thought of transforming the input number into a string tmp, and checking if the string is equal to its reverse.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        return tmp == tmp[::-1]
        
x = 121
sol1=Solution()
print(sol1.isPalindrome(x))