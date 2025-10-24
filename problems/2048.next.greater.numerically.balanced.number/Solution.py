from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        curr = n+1
        while True:
            flag = True
            tmp = str(curr)
            occorrenze = Counter(tmp)
            
            for key in occorrenze.keys():
                if int(occorrenze[key]) != int(key):
                    flag = False
                    
            if flag:
                break
            
            curr += 1
            
        return curr
    
n = 1
sol = Solution()
print(sol.nextBeautifulNumber(n))