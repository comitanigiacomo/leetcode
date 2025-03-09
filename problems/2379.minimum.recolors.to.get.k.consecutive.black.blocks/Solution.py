class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        pos = 0
        result = k
        for i in range(0, len(blocks)):
            if blocks[i] == 'W': white += 1
            if i >= k-1:
                result = min(result, white)
                if blocks[pos] == 'W': white -= 1
                pos += 1
        
        return result
        
blocks = "WBBWWBBWBW"
k = 7
print(Solution().minimumRecolors(blocks, k))