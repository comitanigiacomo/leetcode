from ast import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for elem in words: 
            if self.isPalindrome(elem):
                return elem
        return ""


    def isPalindrome(self, s) -> bool:
        return s == s[::-1]

        