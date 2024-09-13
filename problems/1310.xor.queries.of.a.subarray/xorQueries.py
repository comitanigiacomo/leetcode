from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            prefixXor[i] = prefixXor[i - 1] ^ arr[i - 1]
        
        answer = []
        for left, right in queries:
            result = prefixXor[right + 1] ^ prefixXor[left]
            answer.append(result)
        
        return answer
        
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
sol = Solution()
print(sol.xorQueries(arr, queries))