from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rests = [0]*k

        for elem in arr:
            tmp = elem % k 
            print(elem, tmp)
            rests[tmp] += 1

        rests = rests[1:]
        for i in range(len(rests)):
            if rests[i] != rests[len(rests)-1-i]:
                return False
            
        if (len(rests) % 2 )!= 0:
            if (rests[int(len(rests)/ 2)] )% 2 != 0: return False
        return True
        
arr = [1,2,3,4,5,6]
k = 7
sol = Solution()
print(sol.canArrange(arr,k))