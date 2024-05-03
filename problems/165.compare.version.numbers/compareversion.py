class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        len_diff = abs(len(v1) - len(v2))
        
        if len(v1) < len(v2):
            v1 += ['0'] * len_diff
        elif len(v1) > len(v2):
            v2 += ['0'] * len_diff

        for i in range(len(v1)):
            rev1 = int(v1[i])
            rev2 = int(v2[i])
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        return 0
        
        
version1 = "1.2"
version2 = "1.10"
sol1 = Solution()
print(sol1.compareVersion(version1, version2))